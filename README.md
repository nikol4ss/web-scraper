## Web-Scraper API

Price monitoring microservice with dynamic scraping via Selenium, data processing with Pandas and RESTful endpoints with FastAPI.

### Technologies
- **FastAPI** – exposing REST endpoints.
- **Selenium** – automated scraping.
- **Pandas** – manipulation and analysis of tabular data.
- **Uvicorn** – ASGI server for local execution.

## Installation

```bash
git clone https://github.com/user/web-scraper.git
cd web-scraper
pip install -r requirements.txt
```

**! You must have ChromeDriver installed and compatible with your version of Chrome.**

### Endpoints
Starts scraping and saves data to CSV.
````bash
GET /scrape/{product}
`````

Returns historical and average prices.
```bash
GET /prices/{product}
````

### Improvements to implement

- Support for multiple sources (Amazon, Americanas).
- Relational database (PostgreSQL + SQLAlchemy).
- Dashboard with graphs (Plotly, Streamlit).
- Asynchronous scraping (Playwright)
