# shopify-api-clone

This is part of the technical interview for backend developer candidates for Coop Commerce.

## Setup

1. Clone this repo and `cd` into it
2. Create the virtual environment: `python3 -m venv venv`
3. Enter the virtual environment: `source venv/bin/activate`
4. Download the necessary packages: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Run the server: `python manage.py runserver`


## Test cases

1. `POST` /api/stores creates a store.  
```bash
Request:   
    {
        "name": "Second Store"
    }

Response:
    {
        "id": 1,
        "products": [],
        "category": null,
        "created_at": "2020-08-17T16:26:37.733750Z",
        "updated_at": "2020-08-17T16:26:37.733792Z",
        "name": "Second Store",
        "is_active": true
    }
```
2. `POST` /api/users creates a user.
```bash
Request:
    {
       "username": "gajendrakhatri",
       "password": "hello"
    }

Response:
    {
        "id": 2,
        "categories": [],
        "last_login": null,
        "is_superuser": false,
        "username": "gajendrakhatri",
        "first_name": "",
        "last_name": "",
        "email": "",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2020-08-17T16:37:51.697835Z",
        "created_at": "2020-08-17T16:37:51.698100Z",
        "updated_at": "2020-08-17T16:37:51.698122Z",
        "groups": [],
        "user_permissions": []
    }
```
3. `POST` /api/purchases creates a purhase.
```bash
Request:
    {
        "user_id": 1,
        "details": [{
            "product": 1,
            "quantity": 2
        }]
    }

Response:
    {
        "id": 1,
        "user": {
            "id": 1,
            "categories": [],
            "last_login": "2020-08-17T16:35:08.635774Z",
            "is_superuser": true,
            "username": "khatri94",
            "first_name": "",
            "last_name": "",
            "email": "khatri.gajendra1994@gmail.com",
            "is_staff": true,
            "is_active": true,
            "date_joined": "2020-08-17T16:34:57.862960Z",
            "created_at": "2020-08-17T16:34:57.977079Z",
            "updated_at": "2020-08-17T16:34:57.977095Z",
            "groups": [],
            "user_permissions": []
        },
        "purchase_details": [
            {
                "id": 1,
                "product": {
                    "id": 1,
                    "created_at": "2020-08-17T16:35:27.883120Z",
                    "updated_at": "2020-08-17T16:39:54.018643Z",
                    "name": "First Product",
                    "quantity": 98,
                    "is_active": true,
                    "store": 1
                },
                "created_at": "2020-08-17T16:39:54.021719Z",
                "updated_at": "2020-08-17T16:39:54.021773Z",
                "quantity": 2,
                "purchase": 1
            }
        ],
        "created_at": "2020-08-17T16:39:54.013144Z",
        "updated_at": "2020-08-17T16:39:54.013174Z"
    }
```
4. `GET` /api/stores/1 retrieves a store. Each store has a list of products and a category.
```
Response
    {
        "id": 1,
        "products": [
            {
                "id": 1,
                "created_at": "2020-08-17T16:35:27.883120Z",
                "updated_at": "2020-08-17T16:35:27.883211Z",
                "name": "First Product",
                "quantity": 100,
                "is_active": true,
                "store": 1
            }
        ],
        "category": {
            "id": 1,
            "created_at": "2020-08-17T16:35:36.447332Z",
            "updated_at": "2020-08-17T16:35:36.447367Z",
            "name": "Women under 30",
            "is_active": true
        },
        "created_at": "2020-08-17T16:26:37.733750Z",
        "updated_at": "2020-08-17T16:35:42.048965Z",
        "name": "Second Store",
        "is_active": true
    }

```
5. `GET` /api/users/1 retrieves a user. Each user has a list of preferences.
```bash
Response:
    {
        "id": 1,
        "categories": [
            {
                "id": 1,
                "created_at": "2020-08-17T16:35:36.447332Z",
                "updated_at": "2020-08-17T16:35:36.447367Z",
                "name": "Women under 30",
                "is_active": true
            },
            {
                "id": 2,
                "created_at": "2020-08-17T16:42:37.226497Z",
                "updated_at": "2020-08-17T16:42:37.226540Z",
                "name": "Men over 30",
                "is_active": true
            }
        ],
        "last_login": "2020-08-17T16:35:08Z",
        "is_superuser": true,
        "username": "khatri94",
        "first_name": "",
        "last_name": "",
        "email": "khatri.gajendra1994@gmail.com",
        "is_staff": true,
        "is_active": true,
        "date_joined": "2020-08-17T16:34:57Z",
        "created_at": "2020-08-17T16:34:57.977079Z",
        "updated_at": "2020-08-17T16:42:44.462643Z",
        "groups": [],
        "user_permissions": []
    }
```
6. `GET` /api/purchases/1 retrieves a purhase.
```bash
Response:
    {
        "id": 1,
        "user": {
            "id": 1,
            "categories": [
                {
                    "id": 1,
                    "created_at": "2020-08-17T16:35:36.447332Z",
                    "updated_at": "2020-08-17T16:35:36.447367Z",
                    "name": "Women under 30",
                    "is_active": true
                },
                {
                    "id": 2,
                    "created_at": "2020-08-17T16:42:37.226497Z",
                    "updated_at": "2020-08-17T16:42:37.226540Z",
                    "name": "Men over 30",
                    "is_active": true
                }
            ],
            "last_login": "2020-08-17T16:35:08Z",
            "is_superuser": true,
            "username": "khatri94",
            "first_name": "",
            "last_name": "",
            "email": "khatri.gajendra1994@gmail.com",
            "is_staff": true,
            "is_active": true,
            "date_joined": "2020-08-17T16:34:57Z",
            "created_at": "2020-08-17T16:34:57.977079Z",
            "updated_at": "2020-08-17T16:42:44.462643Z",
            "groups": [],
            "user_permissions": []
        },
        "purchase_details": [
            {
                "id": 1,
                "product": {
                    "id": 1,
                    "created_at": "2020-08-17T16:35:27.883120Z",
                    "updated_at": "2020-08-17T16:39:54.018643Z",
                    "name": "First Product",
                    "quantity": 98,
                    "is_active": true,
                    "store": 1
                },
                "created_at": "2020-08-17T16:39:54.021719Z",
                "updated_at": "2020-08-17T16:39:54.021773Z",
                "quantity": 2,
                "purchase": 1
            }
        ],
        "created_at": "2020-08-17T16:39:54.013144Z",
        "updated_at": "2020-08-17T16:39:54.013174Z"
    }
```

## Bonus
``` bash
Idea: If a person A likes items 1, 2, 3 and B like 2,3,4 then they have similar interests and A should like item 4 and B should like item 1.
This algorithm is entirely based on the past behavior and not on the context. So main idea is to find the similarity score between product to other products or user to other users

Basic assumptions: Customers who had similar tastes in the past, will have similar tastes in the future

Examples:
Product recommendations by e-commerce player like Amazon and merchant recommendations by banks like American Express.

Approach:
User-User Collaborative filtering ->create item to item co-ouccrance matrix
Item-Item Collaborative filtering ->create item to item co-ouccrance matrix

Similarity:most used matrices are Cosine similarity/ jaccard similarity etc

Once user viewed the an item, we can recommend the item similar to that item from item to item silimilarity or we can recommend the item viewed by user similar to the current user
```

