
from fastapi import FastAPI
from app.api.v1.routes  import users, products 
from app.core.config import settings 



app = FastAPI(
    title=settings.Uniqluxe_SHOES , 
    #version=settings.VERSION,
    #dummy_url= f"{settings.API_PREFIX}
)

app.include_router(users.router, prefix=settings.API_PREFIX)
app.include_router(products.router, prefix=settings.API_PREFIX)

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(
        "app.main:app", 
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
    