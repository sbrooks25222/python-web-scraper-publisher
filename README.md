# Python Web Scraper & Local Publisher

A modular Python automation project that scrapes content from a public website, structures the data, and publishes it as formatted blog-ready HTML files.

This project demonstrates a complete automation pipeline:
- Web scraping
- Data cleaning and formatting
- Content publishing
- Clean project structure and documentation

Built as a reusable foundation for content automation, blogging workflows, and future API-based publishing (e.g., Google Blogger).

---

## 🚀 Features

- Scrapes quotes, authors, and tags from a public, scrape-friendly website
- Stores raw scraped data in CSV format
- Converts scraped data into formatted blog post content
- Publishes each item as a standalone HTML file
- Modular architecture (scraper → formatter → publisher)
- Easy to extend to APIs (Blogger, WordPress, CMS, etc.)

---

## 🗂 Project Structure

Blogger_scrapper/
│
├── Scraper/
│ └── scraper_quotes.py # Main scraper script
│
├── formatter/
│ └── format_posts.py # Converts CSV data into blog-ready posts
│
├── publisher/
│ └── local_publisher.py # Saves posts as HTML files locally
│
├── data/
│ └── quotes.csv # Scraped raw data (ignored in git)
│
├── output/
│ └── post_*.html # Generated blog posts (ignored in git)
│
├── requirements.txt
├── .gitignore
└── README.md


---

## 🧠 How It Works

1. **Scraping**
   - Uses `requests` + `BeautifulSoup`
   - Extracts quote text, author, tags, source URL, and timestamp
   - Saves results to a CSV file

2. **Formatting**
   - Reads CSV into Pandas
   - Converts each row into structured blog post content (HTML)

3. **Publishing**
   - Writes each post to an individual `.html` file
   - Ready for upload to Blogger, WordPress, or CMS platforms

---

## ▶️ How to Run

### 1️⃣ Install dependencies

pip install -r requirements.txt

2️⃣ Run the scraper module

python -m Scraper.scraper_quotes

3️⃣ Output

Scraped data saved to:


data/quotes.csv
Generated blog posts saved to:


output/post_1.html
output/post_2.html
...
🛠 Technologies Used
Python 3

Requests

BeautifulSoup

Pandas

CSV / HTML output

Modular Python architecture

🔒 Notes on Ethics & Safety
Scrapes only a public, scrape-friendly website

No login, authentication, or rate-limit bypassing

Designed to follow ethical scraping practices

🔮 Future Improvements
Publish directly to Google Blogger via API

Add scheduling (cron / task scheduler)

Add logging and error recovery

Support additional content sources

Dockerized deployment

👨‍💻 Author
Shawn Brooks
Python Automation & Web Scraping Developer

GitHub: https://github.com/sbrooks25222

LinkedIn: https://www.linkedin.com/in/shawn-brooks-2b84818b

