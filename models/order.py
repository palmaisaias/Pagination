from database import Base, db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Date, ForeignKey
from datetime import date

from models.product import order_products
from sqlalchemy.ext.declarative import declared_attr

class Orders(Base):
    __tablename__ = 'Orders'

    id = Column(Integer, primary_key=True)
    order_date = Column(Date, nullable=False, default=date.today)
    customer_id = Column(Integer, ForeignKey('Customer.id'))

    @declared_attr
    def customer(cls):
        return relationship('Customer', back_populates='orders')

    products = relationship('Products', secondary=order_products, back_populates='orders')