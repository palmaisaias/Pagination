from flask import request, jsonify
from services import order_service
from models.schemas.order_schema import order_schema, orders_schema
from models.schemas.product_schema import products_schema
from models.order import Orders
from database import db
from sqlalchemy import select
from marshmallow import ValidationError

def save_order():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    new_order = order_service.save_order(order_data)
    return jsonify({"id": new_order.id, "Message": "It's on the way!"}), 201

def get_order_items(id):
    query = select(Orders).filter(Orders.id == id)
    order = db.session.execute(query).scalar()
    return products_schema.jsonify(order.products)

def find_all_orders():
    orders = order_service.find_all_orders()
    return orders_schema.jsonify(orders), 200

def find_all_paginate():
    page = int(request.args.get("page"))
    per_page = int(request.args.get("per_page"))
    orders = order_service.find_all_paginate(page, per_page)
    return orders_schema.jsonify(orders), 200
