from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import HTMLResponse , RedirectResponse
from app.database import engine ,Base
from app import models
from app.routers import customer,product ,factor ,factor_details

#doocs_url=None , redoc_url=None, 
app = FastAPI(description='this project writed by zahra bahman' , version='1.0.0')




# app.mount("/static", StaticFiles(directory="app/static"), name="static")



# @app.get("/docs", include_in_schema=False)
# async def docs_redirect():
#     return RedirectResponse(url="/offline-docs")

# @app.get("/offline-docs", response_class=HTMLResponse , include_in_schema=False)
# async def offline_docs():
#     with open("app/offline_docs.html", "r", encoding="utf-8") as f:
#         return f.read()
    
@app.get("/")
def read_root():
    return {"message": "Hello World"}    

Base.metadata.create_all(bind=engine)

app.include_router(customer.router)
app.include_router(product.router)
app.include_router(factor.router)
app.include_router(factor_details.router)


# from app.schemas import CustomerCreate
# @app.post("/new_costomer")
# def new_customer(customer:CustomerCreate):
#     c1=customer.copy()
#     return c1