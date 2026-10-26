from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from app.database import get_db
import app.crud as crud
from app.schemas import *

router=APIRouter(
    prefix="/factor_details",
    tags=['factor_details']
)

@router.post('/',response_model=Factor_detailsOut)
def create_factor_details(factor_details:Factor_detailsCreate,db:Session=Depends(get_db)):
    new_factor_details=crud.create_factor_details(db=db ,factor=factor_details)
    return new_factor_details

@router.get('/',response_model=list[Factor_detailsOut])
def read_factor_details(db:Session=Depends(get_db)):
    factor_detailss=crud.get_factor_details(db)
    return factor_detailss 

@router.get('/{id}',response_model=Factor_detailsOut)
def read_factor_details(id:int,db:Session=Depends(get_db)):
    factor_details=crud.get_factor_details_by_id(db,id=id)
    if factor_details is None:
        raise HTTPException(status_code=404,detail="factor_details not found")
    return factor_details

@router.put('/{id}',response_model=Factor_detailsOut)
def update_factor_details(id:int,updated_factor_details:Factor_detailsCreate,db:Session=Depends(get_db)):
    db_factor_details=crud.update_factor_details(db,id=id,factor=updated_factor_details)
    if db_factor_details is None:
        raise HTTPException(status_code=404,detail="factor_details not found")
    return db_factor_details

@router.delete('/{id}')
def delete_factor_details(id:int,db:Session=Depends(get_db)):
    deleted=crud.delete_factor_details(db,id=id)
    if not deleted:
        raise HTTPException(status_code=404,detail="factor_details not found")
    return {"detail":"factor_details deleted successfully"}

@router.delete('/')
def delete_all_factor_details(db:Session=Depends(get_db)):
    crud.delete_all_factor_details(db)
    return {"detail":" factor_details deleted successfully"}