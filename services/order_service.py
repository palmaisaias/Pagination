from database import db
from models.order import Orders
from models.product import Products
from sqlalchemy import select
from datetime import date

def save_order(order_data):
    new_order = Orders(order_date=date.today(), customer_id=order_data['customer_id'])

    for item_id in order_data['items']:
        query = select(Products).filter(Products.id == item_id)
        item = db.session.execute(query).scalar()
        new_order.products.append(item)

    db.session.add(new_order)
    db.session.commit()
    db.session.refresh(new_order)
    return new_order

def find_all_orders():
    query = select(Orders)
    all_orders = db.session.execute(query).scalars().all()
    return all_orders
