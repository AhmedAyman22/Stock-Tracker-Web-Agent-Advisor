# Stock Tracker — Web Agent Advisor

A web app that scrapes the top NASDAQ companies, lets a user pick up to three tickers, and uses an LLM agent (Gemini) to generate a short buy/hold/sell-style report based on recent price performance.

## How it works

1. **Scraper** (`scraper/scraper.py`) — uses Selenium to pull the top 100 NASDAQ companies by market cap into `data/data.json`.
2. **Frontend** (`app/`) — a Flask app serves a Tailwind-styled page listing the scraped companies, where the user selects up to 3 tickers.
3. **Fetcher** (`api/stock_performance_fetcher.py`) — on submission, fetches each selected ticker's last 3 days of price data via the [Polygon.io](https://polygon.io/) API.
4. **Agent** (`agent/agent.py`) — sends that price data to Gemini with a system prompt configured as a stock advisor persona, and returns a short natural-language report recommending buy/hold/sell.

## Tech stack

- **Backend:** Python, Flask
- **Scraping:** Selenium, webdriver-manager
- **Market data:** Polygon.io API
- **AI:** Google Gemini (`gemini-2.0-flash`)
- **Frontend:** HTML, Tailwind CSS, vanilla JS

## Setup

```bash
git clone https://github.com/AhmedAyman22/Stock-Tracker-Web-Agent-Advisor.git
cd Stock-Tracker-Web-Agent-Advisor

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your own API keys:

```bash
cp .env.example .env
```

You'll need:
- A [Polygon.io](https://polygon.io/) API key (free tier works for basic aggregates)
- A [Google AI Studio](https://aistudio.google.com/) API key for Gemini

## Usage

```bash
python app/app.py
```

Then open `http://localhost:5000`.

- The company list loads from `data/data.json`. Click **Refresh Data** to re-run the scraper and pull a fresh top-100 list.
- Select up to 3 companies and click **Submit Selected Tickers to Advisor** to get a generated report.
- **Clear Selected Tickers** resets your selection.

## Project structure

```
app/        Flask app, routes, templates, static assets
api/        Polygon.io price-fetching logic
agent/      Gemini-based report generation
scraper/    Selenium scraper for NASDAQ top-100 list
data/       Cached scrape results and generated reports (JSON)
```

## Known limitations

- The scraper relies on fixed XPath selectors against the live Nasdaq screener page, so it will break if Nasdaq changes their page markup — there's no fallback selector strategy.
- No automated tests yet.
- The advisor's system prompt is written in a deliberately casual, informal voice — fun for a demo, but it's a stylistic choice rather than the tone you'd want for a real financial-advice product.
- This is a personal project for demonstration purposes, not financial advice software — outputs shouldn't be used for real investment decisions.

## Author

Ahmed Ayman
