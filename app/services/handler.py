import os
import pandas as pd
from app.model import PriceResponse

def capture_price(product: str) -> PriceResponse:
    csv_path = f"data/{product}.csv"

    if not os.path.exists(csv_path):
        return PriceResponse(product=product, history=[], average_price=0)

    df = pd.read_csv(csv_path, parse_dates=["timestamp"])
    listing_price = df['price'].mean()

    return PriceResponse(
        product=product,
        history=df.to_dict(orient='records'),
        average_price=round(listing_price, 2)
    )
