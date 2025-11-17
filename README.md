📰 News Headlines Web Scraper
This project is a Python-based web scraper designed to collect top news headlines from a public website such as BBC News. The script uses the requests library to fetch webpage content and BeautifulSoup to parse and extract headline elements identified by <h2> tags.

Once the headlines are extracted, the program automatically saves them into a headlines.txt file, allowing the data to persist even after the script completes. This makes the project useful for automating news collection and practicing real-world scraping workflows.

The task demonstrates core concepts such as HTTP requests, HTML parsing, file handling, and process automation. To run the project, install dependencies and execute the script using: python news_scraper.py.

📦 Requirements
Install dependencies using:

pip install requests beautifulsoup4

🚀 Features

✔ Fetches real-time headlines from a live news website
✔ Parses HTML and extracts <h2> headline elements
✔ Saves results automatically into a text file
✔ Beginner-friendly and fully commented code