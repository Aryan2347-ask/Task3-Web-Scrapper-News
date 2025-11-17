import requests
from bs4 import BeautifulSoup

# URL of news site (You can change to any public site)
URL = "https://www.bbc.com/news"  

def fetch_headlines():
    """Fetch and scrape top news headlines from the website."""
    
    response = requests.get(URL)

    # Check if request was successful
    if response.status_code != 200:
        print("Failed to fetch webpage!")
        return []

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines (BBC uses <h2> tags for headlines)
    headlines = [headline.get_text(strip=True) for headline in soup.find_all("h2")]

    return headlines


def save_to_file(headlines):
    """Save scraped headlines to a text file."""
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for line in headlines:
            file.write(line + "\n")

    print("Headlines saved to headlines.txt")


def main():
    print("Fetching headlines...")

    headlines = fetch_headlines()

    if headlines:
        print(f"Scraped {len(headlines)} headlines.")
        save_to_file(headlines)
    else:
        print("No headlines found.")


if __name__ == "__main__":
    main()
