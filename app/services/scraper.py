import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_product(product: str):
    driver = webdriver.Chrome()
    search = f"https://www.mercadolivre.com.br/{product.replace(" ", "-")}"

    driver.get(search)
    time.sleep(3)

    try:
        title = driver.find_element(By.CSS_SELECTOR, '#header-octopus > div > div.ui-pdp-header__title-container > h1').text
        price = driver.find_element(By.CSS_SELECTOR, '#price > div > div.ui-pdp-price__main-container > div.ui-pdp-price__second-line').text

    except:
        driver.quit()
        raise Exception("Product not found")

    df = pd.DataFrame([{
        "product": product,
        "title": title,
        "price": float(price.replace("R$", "").replace(".", "").replace(",", ".").strip()),
        "timestamp": pd.Timestamp.now()
    }])

    csv_path = f"data/{product}.csv"
    os.makedirs("data", exist_ok=True)

    if os.path.exists(csv_path):
        df.to_csv(csv_path, mode="a", header=False, index=False)

    else:
        df.to_csv(csv_path, index=False)

    driver.quit()
