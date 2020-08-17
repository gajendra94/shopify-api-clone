from rest_framework import serializers
from api.models import Store, Purchase, User, Product, Category, PurchaseDetail
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


# Store Serializer
class StoreSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Store
        fields = '__all__'
        extra_fields = ['products']


# Purchase Detail Serializer
class PurchaseDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = PurchaseDetail
        fields = '__all__'


# Purchase Serializer
class PurchaseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    purchase_details = PurchaseDetailSerializer(read_only=True, many=True)

    user_id = serializers.IntegerField(write_only=True)
    details = serializers.ListField(write_only=True)

    ''' Function to get the product object '''

    def get_product(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise Http404

    ''' Function to fetch the user details '''

    def validate_user_id(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Http404('User does not exists')

    def validate_purchase_quantity(self, product_id, quantity):
        if not product_id:
            raise serializers.ValidationError('product_id should be present in purchase details.')

        if not quantity:
            raise serializers.ValidationError('quantity should be present in purchase details.')

        product_obj = self.get_product(product_id)
        product_quantity = product_obj.quantity

        if product_quantity < quantity:
            raise serializers.ValidationError('Purchase quantity should be less than the Product available quantity.')

        return quantity

    ''' Validate quantity so the purchase quantity should be less than the product quantity '''
    def validate_details(self, value):
        purchase_details = self.context['request'].data['details']

        if not purchase_details:
            raise serializers.ValidationError('Purchase Details should not be empty.')

        for detail in purchase_details:
            self.validate_purchase_quantity(detail['product'], detail['quantity'])

        return value

    ''' Updating product quantity also while creating the purchase '''
    def create(self, validated_data):
        user = validated_data.get('user_id')
        purchase_details = validated_data.pop('details')

        purchase = Purchase.objects.create(user=user)

        for detail in purchase_details:
            product_obj = self.get_product(detail['product'])
            product_quantity = product_obj.quantity

            ''' Updating the quantity at the product '''
            product_obj.quantity = product_quantity-detail['quantity']
            product_obj.save()
            PurchaseDetail.objects.create(purchase=purchase, product_id=detail['product'], quantity=detail['quantity'])

        return purchase

    class Meta:
        model = Purchase
        fields = '__all__'
