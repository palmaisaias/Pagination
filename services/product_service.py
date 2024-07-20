from database import db
from models.product import Products
from sqlalchemy import select

def save_product(product_data):
    new_product = Products(
        product_name=product_data['product_name'], 
        price=product_data['price']
    )
    db.session.add(new_product)
    db.session.commit()
    db.session.refresh(new_product)
    return new_product

def find_all_products():
    query = select(Products)
    all_products = db.session.execute(query).scalars().all()
    return all_products

def find_all_paginate(page, per_page):
    products = db.paginate(select(Products), page=page, per_page=per_page)
    return products