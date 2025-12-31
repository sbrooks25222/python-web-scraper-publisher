import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timezone
from publisher.local_publisher import publish_locally
from formatter.format_posts import format_posts


BASE_URL = "https://quotes.toscrape.com"


def scrape_quotes(pages: int = 5) -> pd.DataFrame:
    """
    Scrape quotes, authors, and tags from quotes.toscrape.com
    """
    all_quotes = []

    for page in range(1, pages + 1):
        url = f"{BASE_URL}/page/{page}/"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"Failed to fetch page {page}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.select(".quote")

        for quote in quotes:
            text = quote.select_one(".text").get_text(strip=True)
            author = quote.select_one(".author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote.select(".tags .tag")]

            all_quotes.append({
                "quote": text,
                "author": author,
                "tags": ", ".join(tags),
                "source_url": url,
                "scraped_at": datetime.now(timezone.utc).isoformat()
            })

        print(f"Scraped page {page}")

    return pd.DataFrame(all_quotes)


def save_quotes_csv(df: pd.DataFrame, path: str = "data/quotes.csv"):
    df.to_csv(path, index=False)
    print(f"Saved {len(df)} quotes to {path}")


def df_to_posts(df: pd.DataFrame) -> list:
    """
    Convert DataFrame rows into publishable post objects
    """
    posts = []

    for _, row in df.iterrows():
        posts.append({
            "title": f"Inspirational Quote — {row['author']}",
            "content": f"""
                <blockquote>{row['quote']}</blockquote>
                <p><strong>Author:</strong> {row['author']}</p>
                <p><strong>Tags:</strong> {row['tags']}</p>
            """
        })

    return posts


if __name__ == "__main__":
    df = scrape_quotes(pages=5)
    save_quotes_csv(df)

    posts = format_posts(df)
    publish_locally(posts)


