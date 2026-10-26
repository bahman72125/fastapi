from pydantic import BaseModel,ConfigDict
from typing import List
from datetime import datetime
from .factor_details import Factor_detailsOut

class FactorBase(BaseModel):
    cid:int
    
    


class FactorCreate(FactorBase):
    pass

class FactorOut(FactorBase):
    id:int
    date:datetime
    
    factor_d:List[Factor_detailsOut]
    model_config=ConfigDict(from_attributes=True)


