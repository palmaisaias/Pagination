from database import db
from models.customer import Customer
from sqlalchemy import select

def save_customer(customer_data):
    new_customer = Customer(
        customer_name=customer_data['customer_name'], 
        email=customer_data['email'], 
        phone=customer_data['phone']
    )
    db.session.add(new_customer)
    db.session.commit()
    db.session.refresh(new_customer)
    return new_customer

def find_all_customers():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers
