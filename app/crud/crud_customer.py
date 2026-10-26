from sqlalchemy.orm import session
from sqlalchemy import select,func
from app.models import Customer
import app.schemas as schemas
from app.utils import security


def create_customer(db:session ,customer:schemas.CustomerCreate ):
    password_hash=security.hash_password(customer.password)
    db_customer=Customer(
        username=customer.username,
        password=password_hash
        
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def get_customer(db:session):
    sql=select(Customer).where().order_by(Customer.username)
    return db.scalars(sql).all()

def get_customer_by_id(db:session,id=id):
    sql=select(Customer).where(id==id)
    return db.scalars(sql).first()

def get_customer_max_id(db: session):
    sql = select(func.max(Customer.id))
    return db.scalar(sql)

def delete_customer(db:session ,id:int) :
    customer=db.get(Customer,id)
    if customer:
        db.delete(customer)
        db.commit()
        return customer
    else:
        return None  

def delete_all_customers(db:session):
    db.query(Customer).delete()
    db.commit() 

def update_customer(db:session,id:int,customer:schemas.CustomerCreate):
    db_customer=db.get(Customer,id)
    if db_customer: 
       db_customer.username=customer.username
       db_customer.password=customer.password
       db.commit()
       return db_customer
    else:
       return None        