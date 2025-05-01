
from fastapi import FastAPI
#from app.api.v1.routes   
from app.api.core.config import settings 
from sqlalchemy import create_engine


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

#app.include_router(users.router, prefix=settings.API_PREFIX)
#app.include_router(products.router, prefix=settings.API_PREFIX)
@app.get("/")
async def root():
    return{
        "message": f"welcome to {settings.PROJECT_NAME}",
        "version": settings.VERSION
    }
@app.on_event("startup")
async def startup():
    async with engine.connect() as conn:
        print("Connected to PostgreSQL database")


if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(
        "app.main:app", 
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
