from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Factor(Base):
    __tablename__ = 'factor'

    id=Column(Integer ,primary_key=True ,index=True)
    cid=Column(Integer ,ForeignKey('customer.id'))
    date=Column(DateTime ,default=datetime.utcnow)
    #jalalidate=Column(String,default='')

    customer=relationship("Customer",back_populates='factors')
    factor_d=relationship("Factor_details",back_populates='factord')
    