from pydantic import BaseModel,ConfigDict


class Factor_detailsBase(BaseModel):
    fid:int
    pid:int
    no:int
    total:int
    


class Factor_detailsCreate(Factor_detailsBase):
    pass

class Factor_detailsOut(Factor_detailsBase):
    id:int

    model_config=ConfigDict(from_attributes=True)


