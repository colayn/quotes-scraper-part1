# 📊 Quotes Scraper Part 1

## 📌 Overview
This project is a Python web scraper that extracts quotes from:

http://quotes.toscrape.com/search.aspx

It uses Playwright (sync API) to automate dropdown selection and scrape structured data.

---

## 📦 Data Extracted

For each quote, the script collects:

- 📝 Quote text  
- 👤 Author  
- 🏷️ Tags associated with the quote  

---

## ⚙️ Tech Stack

- Python 3.10+
- Playwright (Sync API)
- JSON (output format)

---

## 🧠 How the Scraper Works

The scraper is organized into modular functions:

### 1. `authors_get(page)`
- Navigates to the site
- Extracts all available authors from dropdown

### 2. `tags_get(page, author)`
- Selects an author
- Waits for tags to load dynamically
- Extracts available tags

### 3. `parse_quote(div, fallback_author)`
- Parses:
  - Quote text
  - Author
  - Tags from each quote block

### 4. `scrape_all_quotes()`
- Loops through:
  - All authors
  - All tags per author
- Extracts unique quotes
- Prevents duplicates using a `seen` set

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/colayn/quotes-scraper-part1.git
cd quotes-scraper-part1
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Linux / macOS
# venv\Scripts\activate    # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Run the scraper

```bash
python scraper_pw3.py
```

## 📤 Output

After running the script, a file is generated:
```bash
quotes_output.json
```

## JSON Structure
```bash
[
  {
    "quote": "Be yourself; everyone else is already taken.",
    "author": "Oscar Wilde",
    "tags": ["inspirational", "life", "humor"]
  }
]
```
