from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = 'product'

    id=Column(Integer ,primary_key=True ,index=True)
    price=Column(Integer,nullable=False)
    name=Column(String,nullable=False)

 
    factor_d_product=relationship("Factor_details",back_populates='product')