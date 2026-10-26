from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from app.database import get_db
import app.crud  as crud
from app.schemas import *

router=APIRouter(
    prefix="/customer",
    tags=['customer']
)

@router.post('/',response_model=CustomerOut)
def create_customer(customer:CustomerCreate,db:Session=Depends(get_db)):
    new_customer=crud.create_customer(db=db ,customer=customer)
    return new_customer

@router.get('/',response_model=list[CustomerOut])
def read_customer(db:Session=Depends(get_db)):
    customers=crud.get_customer(db)
    return customers 


@router.get('/max')
def read_customer_id(db: Session = Depends(get_db)):
    customer_id = crud.get_customer_max_id(db)
    if customer_id is None:
        raise HTTPException(status_code=404,detail="customer not found")
    return customer_id


@router.get('/{id}',response_model=CustomerOut)
def read_customer_id(id:int,db:Session=Depends(get_db)):
    customer=crud.get_customer_by_id(db,id=id)
    if customer is None:
        raise HTTPException(status_code=404,detail="customer not found")
    return customer

@router.put('/{id}',response_model=CustomerOut)
def update_customer(id:int,updated_customer:CustomerCreate,db:Session=Depends(get_db)):
    db_customer=crud.update_customer(db,id=id,customer=updated_customer)
    if db_customer is None:
        raise HTTPException(status_code=404,detail="customer not found")
    return db_customer

@router.delete('/{id}')
def delete_customer(id:int,db:Session=Depends(get_db)):
    deleted=crud.delete_customer(db,id=id)
    if not deleted:
        raise HTTPException(status_code=404,detail="customer not found")
    return {"detail":"customer deleted successfully"}

@router.delete('/')
def delete_all_customers(db:Session=Depends(get_db)):
    crud.delete_all_customers(db)
    return {"detail":"customers deleted successfully"}