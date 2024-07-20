from database import Base, db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey

order_products = Table(
    'Order_Products',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('Orders.id'), primary_key=True),
    Column('product_id', Integer, ForeignKey('Products.id'), primary_key=True)
)

class Products(Base):
    __tablename__ = 'Products'

    id = Column(Integer, primary_key=True)
    product_name = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)
    orders = relationship('Orders', secondary=order_products, back_populates='products')