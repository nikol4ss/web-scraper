from fastapi import APIRouter
from app.services import scrape_product
from app.services.handler import get_price_history
from model import PriceResponse

router = APIRouter()

@router.get("/scrape/{product}")
def scrape(product: str):
    scrape_product(product)
    return {"message": f"Scraping iniciado para '{product}'."}

@router.get("/prices/{product}", response_model=PriceResponse)
def prices(product: str):
    return get_price_history(product)
