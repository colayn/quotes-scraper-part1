# Quotes Scraper – Technical Screening Task

## 📌 Overview
This project is a Python-based web scraper that extracts quotes from:

http://quotes.toscrape.com/search.aspx

It collects the following data:
- Quote text
- Author
- Associated tags

The script handles pagination to ensure all available quotes are extracted.

---

## ⚙️ Tech Stack
- Python 3
- Requests
- BeautifulSoup4
- Pandas

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/colayn/quotes-scraper.git
cd quotes-scraper
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the script

```bash
python scraper.py
```

## Output
- CSV file containing all scraped quotes with authors and tags

## Notes
- Handles pagination
- Uses retry-safe HTTP requests
- Includes polite scraping delay