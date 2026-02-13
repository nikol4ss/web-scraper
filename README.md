## Web-Scraper API

A price monitoring microservice built with FastAPI that performs dynamic web scraping using Selenium, processes data with Pandas, and exposes RESTful endpoints for retrieving price history and averages.

### About 

This project is a price monitoring microservice designed to scrape product data dynamically using Selenium and process it with Pandas. Built with FastAPI and served via Uvicorn, it exposes RESTful endpoints to trigger scraping operations and retrieve historical and average price data. The service stores results in CSV format and is structured for extensibility. Planned improvements include support for multiple e-commerce sources, integration with a relational database using PostgreSQL and SQLAlchemy, implementation of dashboards with Plotly or Streamlit, and migration to asynchronous scraping with Playwright for better scalability and performance.

### Endpoints
Starts scraping and saves data to CSV.
````bash
GET /scrape/{product}
`````

Returns historical and average prices.
```bash
GET /prices/{product}
````


### Installation

1. Clone this repository:

```bash
git clone https://github.com/user/voting.git
```

2. (Optional but recommended) Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the program
```bash
python main.py
```

<br>
<p align="center" style="opacity:0.6;">
MIT License – see the <a href="LICENSE">LICENSE</a> file for details.
</p>
