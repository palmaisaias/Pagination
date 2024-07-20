from flask import request, jsonify
from services.product_service import save_product, find_all_products
from models.schemas.product_schema import product_schema, products_schema
from marshmallow import ValidationError

def create_product():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_product = save_product(product_data)
    return product_schema.jsonify(new_product), 201

def get_products():
    products = find_all_products()
    return products_schema.jsonify(products), 200