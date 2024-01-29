Overview

This project is a FastAPI-based backend with MongoDB as the database. It provides two APIs - one for retrieving a list of products with pagination (/product) and another for creating orders(/order) with a list of items.

Folder Structure


    project-root
    │   .gitignore
    │   requirements.txt
    │   README.md
    │
    └───app
        │
        ├───controller
        │       product_controller.py
        │       order_controller.py
        │     
        │
        ├───service
        │       product_service.py
        │       order_service.py
        │       
        │
        ├───repository
        │       product_repository.py
        │       order_repository.py
        │       
        │
        ├───utils
        │       helpers.py
        │       
        │
        ├───model
        │       product_model.py
        │       order_model.py
        │       
        │
        ├───runner.py
        │       
        │
        └───extensions.py

Setup

    Clone the repository:

        git clone https://github.com/ultimateshark/cosmocloud-task.git
        cd cosmocloud-task

    Install dependencies:

        pip install -r requirements.txt

    Configure MongoDB:

        Make sure MongoDB is installed and running.
        Update MongoDB connection details in config/db_config.py(I have added a temporary URI for now which has limited access and will be deleted in few days)

    Run the FastAPI application:

        uvicorn app.runner.main:app --reload

Usage:
    Product API (/product)

        Endpoint: /product
        Method: GET
        Parameters:
            offset (optional): Offset for pagination
            limit (optional): Number of items per page
            min_price (optional): Minimum filter for price
            max_pricce (optional): Maximum filter for price
        Response: 
            {
            "data": [
                {
                "product_id": "65b6618c22b322ddce3c27c6",
                "product_name": "Cookware Set",
                "price": 129.99,
                "quantity_available": 35
                },
                {
                "product_id": "65b6618c22b322ddce3c27cb",
                "product_name": "Air Purifier",
                "price": 99.99,
                "quantity_available": 40
                },
                {
                "product_id": "65b6618c22b322ddce3c27b8",
                "product_name": "Fitness Tracker",
                "price": 79.99,
                "quantity_available": 150
                },
                {
                "product_id": "65b6618c22b322ddce3c27b5",
                "product_name": "Laptop",
                "price": 999.99,
                "quantity_available": 40
                },
                {
                "product_id": "65b6618c22b322ddce3c27bb",
                "product_name": "Smartwatch",
                "price": 129.99,
                "quantity_available": 80
                },
                {
                "product_id": "65b6618c22b322ddce3c27d2",
                "product_name": "Back Massager",
                "price": 49.99,
                "quantity_available": 40
                },
                {
                "product_id": "65b6618c22b322ddce3c27cd",
                "product_name": "Cordless Drill",
                "price": 79.99,
                "quantity_available": 60
                },
                {
                "product_id": "65b6618c22b322ddce3c27ce",
                "product_name": "Blender",
                "price": 39.99,
                "quantity_available": 90
                },
                {
                "product_id": "65b6618c22b322ddce3c27bd",
                "product_name": "External Hard Drive",
                "price": 79.99,
                "quantity_available": 60
                },
                {
                "product_id": "65b6618c22b322ddce3c27d1",
                "product_name": "Cooking Utensil Set",
                "price": 29.99,
                "quantity_available": 50
                }
            ],
            "page": {
                "nextOffset": 10,
                "prevOffset": 0,
                "limit": 10,
                "total": 30
            }
            }

    Order API (/order)

        Endpoint: /order
        Method: POST
        Request Body:

        {
        "items": [
            {
            "product_id": "string",
            "quantity": 0
            }
        ],
        "user_address": {
            "city": "string",
            "country": "string",
            "pincode": 0
        }
        }

    Response:


            {
                "_id":"65b69a6f56a60850597eafec",
                "total_amount":4999.95,
                "items":[{"product_id":"65b6618c22b322ddce3c27b5","quantity":5}],
                "createdOn":"2024-01-28 23:48:23.763180",
                "user_address":{"city":"xyz","country":"india","pincode":100000}
            }
