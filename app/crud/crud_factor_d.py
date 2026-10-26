from sqlalchemy.orm import session
from sqlalchemy import select
from app.models import Factor_details
import app.schemas as schemas


def create_factor_details(db:session ,factor:schemas.Factor_detailsCreate ):
    db_factor=Factor_details(
        pid=factor.pid,
        fid=factor.fid,
        no=factor.no,
        total=factor.total
    )
    db.add(db_factor)
    db.commit()
    db.refresh(db_factor)
    return db_factor


def get_factor_details(db:session):
    sql=select(Factor_details).where()
    return db.scalars(sql).all()

def get_factor_details_by_id(db:session,id=id):
    sql=select(Factor_details).where(id==id)
    return db.scalars(sql).first()

def delete_factor_details(db:session ,id:int) :
    factor=db.get(Factor_details,id)
    if factor:
        db.delete(factor)
        db.commit()
        return factor
    else:
        return None  

def delete_all_factor_details(db:session):
    db.query(Factor_details).delete()
    db.commit() 

def update_factor_details(db:session,id:int,factor:schemas.Factor_detailsCreate):
    db_factor=db.get(Factor_details,id)
    if db_factor: 
       db_factor.pid=factor.pid
       db_factor.fid=factor.fid
       db_factor.no=factor.no
       db_factor.total=factor.total
       db.commit()
       return db_factor
    else:
       return None        
