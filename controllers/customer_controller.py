from flask import request, jsonify
from services import customer_service
from models.schemas.customer_schema import customer_schema, customers_schema
from marshmallow import ValidationError

def save():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_customer = customer_service.save(customer_data)
    return customer_schema.jsonify(new_customer), 201

def get_customers():
    customers = customer_service.find_all_customers()
    return customers_schema.jsonify(customers), 200

def find_all_paginate():
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    customers = customer_service.find_all_paginate(page, per_page)
    return customers_schema.jsonify(customers), 200