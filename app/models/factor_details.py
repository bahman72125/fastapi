from sqlalchemy import Column,Integer,ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Factor_details(Base):
    __tablename__ = 'factor_details'

    id=Column(Integer ,primary_key=True ,index=True)
    fid=Column(Integer ,ForeignKey('factor.id'))
    pid=Column(Integer ,ForeignKey('product.id'))
    no=Column(Integer,default=0)
    total=Column(Integer,default=0)


    product=relationship("Product",back_populates='factor_d_product')
    factord=relationship("Factor",back_populates='factor_d')