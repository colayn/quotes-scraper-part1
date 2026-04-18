import json
from playwright.sync_api import sync_playwright

BASE_URL = "http://quotes.toscrape.com/search.aspx"


# -------------------
# GET AUTHORS
# -------------------
def authors_get(page):
    page.goto(BASE_URL)
    options = page.query_selector_all("select#author option")

    authors = []
    for opt in options:
        val = opt.get_attribute("value")
        if val:
            authors.append(val)

    return authors


# -------------------
# GET TAGS
# -------------------
def tags_get(page, author):
    page.goto(BASE_URL)
    page.wait_for_selector("select#author")

    page.select_option("select#author", author)

    page.wait_for_function(
        "document.querySelector('select#tag') && document.querySelector('select#tag').options.length > 1"
    )

    options = page.query_selector_all("select#tag option")

    tags = []
    for opt in options:
        val = opt.get_attribute("value")
        if val:
            tags.append(val)

    return tags


# -------------------
# PARSE QUOTE
# -------------------
def parse_quote(div, fallback_author):
    text = ""
    author_name = fallback_author

    # quote text
    for sel in ["span.text", ".text", "span"]:
        el = div.query_selector(sel)
        if el:
            text = el.inner_text().strip()
            if text:
                break

    # author fallback
    for sel in [".author", "small.author"]:
        el = div.query_selector(sel)
        if el:
            author_name = el.inner_text().strip()

    # tags
    tag_els = div.query_selector_all(".tag")
    tags_list = [t.inner_text().strip() for t in tag_els]

    return {
        "quote": text,
        "author": author_name,
        "tags": tags_list
    }


# -------------------
# MAIN SCRAPER
# -------------------
def scrape_all_quotes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        all_quotes = []
        seen = set()

        authors = authors_get(page)
        print(f"Found {len(authors)} authors")

        for author in authors:
            print(f"Processing: {author}")

            tags = tags_get(page, author)

            for tag in tags:
                try:
                    page.goto(BASE_URL)
                    page.wait_for_selector("select#author")

                    page.select_option("select#author", author)
                    page.wait_for_function(
                        "document.querySelector('select#tag') && document.querySelector('select#tag').options.length > 1"
                    )

                    page.select_option("select#tag", tag)
                    page.click("input.btn[type='submit']")
                    page.wait_for_timeout(1500)

                    quote_divs = page.query_selector_all("div.quote")

                    for div in quote_divs:
                        q = parse_quote(div, author)

                        key = (q["quote"], q["author"])

                        if q["quote"] and key not in seen:
                            seen.add(key)
                            all_quotes.append(q)

                except Exception as e:
                    print(f"Error {author}/{tag}: {e}")

        browser.close()
        return all_quotes


# -------------------
# SAVE JSON
# -------------------
def save_json(data):
    with open("quotes_output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(data)} quotes to quotes_output.json")


# -------------------
# RUN
# -------------------
def main():
    results = scrape_all_quotes()

    print("\n" + "=" * 60)
    print(f"Total quotes: {len(results)}")
    print("=" * 60 + "\n")

    save_json(results)


if __name__ == "__main__":
    main()