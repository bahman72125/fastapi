from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from app.schemas import *
from typing import List

router=APIRouter(
    prefix="/product",
    tags=['product']
)

@router.post('/',response_model=ProductOut)
def create_product(product:ProductCreate,db:Session=Depends(get_db)):
    return crud.create_product(db ,product)

@router.get('/',response_model=list[ProductOut])
def read_product(db:Session=Depends(get_db)):
    return crud.get_product(db)

@router.get('/{id}',response_model=list[ProductOut])
def read_product(id:int,db:Session=Depends(get_db)):
    product=crud.get_product_by_id(db,id=id)
    if not product:
        raise HTTPException(status_code=404,detail="product not found")
    return product

@router.get('/fprice/{fprice}',response_model=list[ProductOut])
def read_product_by_price(fprice:int,db:Session=Depends(get_db)):
    product=crud.get_product_by_fprice(db,fprice)
    if not product:
       raise HTTPException(status_code=404,detail="product not found")
    return product

@router.get('/tprice/{tprice}',response_model=list[ProductOut])
def read_product_by_price(tprice:int,db:Session=Depends(get_db)):
   product1=crud.get_product_by_tprice(db,tprice)
   if not product:
      raise HTTPException(status_code=404,detail="product not found")
   return product1



@router.get('/ftprice/{fprice}/{tprice}',response_model=list[ProductOut])
def read_product_by_price2(fprice:int,tprice:int,db:Session=Depends(get_db)):
    product=crud.get_product_by_fprice_tprice(db,fprice,tprice)
    if not product:
       raise HTTPException(status_code=404,detail="product not found")
    return product

@router.get('/name/{name}',response_model=list[ProductOut])
def read_product_by_name(name:str,db:Session=Depends(get_db)):
    product=crud.get_product_by_name(db,name)
    if not product:
       raise HTTPException(status_code=404,detail="product not found")
    return product

@router.put('/{id}',response_model=ProductOut)
def update_product(id:int,product:ProductCreate,db:Session=Depends(get_db)):
    updated=crud.update_product(db,id,product)
    if  updated is None:
        raise HTTPException(status_code=404,detail="product not found")
    return updated

@router.delete('/{id}')
def delete_product(id:int,db:Session=Depends(get_db)):
    deleted=crud.delete_product(db,id)
    if not deleted:
        raise HTTPException(status_code=404,detail="product not found")
    return {"detail":"product deleted successfully","deleted":deleted}

@router.delete('/')
def delete_all_product(db:Session=Depends(get_db)):
    crud.delete_all_product(db)
    return {"detail":"products deleted successfully"}