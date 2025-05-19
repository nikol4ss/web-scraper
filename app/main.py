from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Price Tracker API")
app.include_router(router)



