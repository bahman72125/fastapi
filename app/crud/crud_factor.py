from sqlalchemy.orm import session
from sqlalchemy import select
from app.models import Factor
import app.schemas as schemas
from datetime import datetime


def create_factor(db:session ,factor1:schemas.FactorCreate ):
    db_factor=Factor(
        cid=factor1.cid,
        date=datetime.utcnow()
    )
    db.add(db_factor)
    db.commit()
    db.refresh(db_factor)
    return db_factor


def get_factor(db:session):
    sql=select(Factor).where()
    return db.scalars(sql).all()

def get_factor_by_id(db,id=id):
    sql=select(Factor).where(id==id)
    return db.scalars(sql).first()

def delete_factor(db:session ,id:int) :
    factor=db.get(Factor,id)
    if factor:
        db.delete(factor)
        db.commit()
        return factor
    else:
        return None  

def delete_all_factors(db:session):
    db.query(Factor).delete()
    db.commit() 

def update_factor(db:session,id:int,factor:schemas.FactorCreate):
    db_factor=db.get(Factor,id)
    if db_factor: 
       db_factor.cid=factor.cid
       db.commit()
       return db_factor
    else:
       return None        
