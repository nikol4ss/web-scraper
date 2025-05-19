from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Price Tracker API")
app.include_router(router)


uvicorn app.main:app --reload
