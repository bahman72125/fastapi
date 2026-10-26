from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from app.database import get_db
import app.crud  as crud
from app.schemas import *

router=APIRouter(
    prefix="/factor",
    tags=['factor']
)

@router.post('/',response_model=FactorOut)
def create_factor1(factor:FactorCreate,db:Session=Depends(get_db)):
    new_factor=crud.create_factor(db=db ,factor1=factor)
    return new_factor

@router.get('/',response_model=list[FactorOut])
def read_factor(db:Session=Depends(get_db)):
    factors=crud.get_factor(db)
    return factors 

@router.get('/{id}',response_model=FactorOut)
def read_factor(id:int,db:Session=Depends(get_db)):
    factor=crud.get_factor_by_id(db,id=id)
    if not factor :
        raise HTTPException(status_code=404,detail="factor not found")
    return factor

@router.put('/{id}',response_model=FactorOut)
def update_factor(id:int,factor:FactorCreate,db:Session=Depends(get_db)):
    updated=crud.update_factor(db,id=id,factor=factor)
    if not updated:
        raise HTTPException(status_code=404,detail="factor not found")
    return updated

@router.delete('/{id}')
def delete_factor(id:int,db:Session=Depends(get_db)):
    deleted=crud.delete_factor(db,id=id)
    if not deleted:
        raise HTTPException(status_code=404,detail="factor not found")
    return {"detail":"factor deleted successfully"}

@router.delete('/')
def delete_all_factors(db:Session=Depends(get_db)):
    crud.delete_all_factors(db)
    return {"detail":"factors deleted successfully"}