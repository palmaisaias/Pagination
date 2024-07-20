from flask import request, jsonify
from services.customer_service import save_customer, find_all_customers
from models.schemas.customer_schema import customer_schema, customers_schema
from marshmallow import ValidationError

def create_customer():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_customer = save_customer(customer_data)
    return customer_schema.jsonify(new_customer), 201

def get_customers():
    customers = find_all_customers()
    return customers_schema.jsonify(customers), 200
