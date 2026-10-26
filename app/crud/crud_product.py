from sqlalchemy.orm import session
from sqlalchemy import select
from app.models import Product
import app.schemas as schemas


def create_product(db:session ,product:schemas.ProductCreate ):
    db_product=Product(
        name=product.name,
        price=product.price
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db:session):
    sql=select(Product).where().order_by(Product.name)
    return db.scalars(sql).all()

def get_product_by_id(db:session,id:int):
    sql=select(Product).where(Product.id==id)
    return db.scalars(sql).all()
  # return db.get(Product,id)

def get_product_by_fprice(db:session,fprice:int):
    sql = select(Product).where(Product.price >= fprice)
    result = db.scalars(sql).all()
    return result


def get_product_by_tprice(db:session,tprice:int):
    sql = select(Product).where(Product.price <= tprice)
    result = db.scalars(sql).all()
    return result

def get_product_by_fprice_tprice(db:session,fprice:int,tprice:int):
    sql = select(Product).where(fprice <= Product.price  , Product.price <= tprice)
    result = db.scalars(sql).all()
    return result


def get_product_by_name(db:session,name:str):
    sql = select(Product).where(Product.name == name)
    result = db.scalars(sql).all()
    return result

def delete_product(db:session ,id:int) :
    product=db.get(Product,id)
    if product:
        db.delete(product)
        db.commit()
        return product
    else:
        return None  

def delete_all_product(db:session):
    db.query(Product).delete()
    db.commit() 
    

def update_product(db:session,id:int,product:schemas.ProductCreate):
    db_product=db.get(Product,id)
    if db_product: 
       db_product.name=product.name
       db_product.price=product.price
       db.commit()
       return db_product
    else:
       return None        
