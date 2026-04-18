# Quotes Scraper Part 1

## 📌 Overview
This project is a Python-based web scraper that extracts quotes from:

http://quotes.toscrape.com/search.aspx

It collects the following data:
- Quote text
- Author
- Associated tags

---

## ⚙️ Tech Stack
- Python 3
- Playwright

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/colayn/quotes-scraper-part1.git
cd quotes-scraper-part1
```

### 2. Install dependencies

```bash
python3 -m venv venv
source venv/bin/activate   # Linux / Ubuntu / macOS
# venv\Scripts\activate    # Windows

pip install -r requirements.txt
playwright install chromium
```

### 3. Run the script

```bash
python scraper.py
```

## Output
- JSON
