from database import Base, db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class Customer(Base):
    __tablename__ = 'Customer'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String(200), nullable=False)
    email = Column(String(300))
    phone = Column(String(16))
    orders = relationship('Orders', back_populates='customer')
