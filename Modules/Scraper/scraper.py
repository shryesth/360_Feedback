from feedparser import parse
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time


def scrape_website(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # Remove script, style, and other non-visible tags
        for tag in soup(
            [
                "script",
                "style",
                "meta",
                "link",
                "noscript",
                "header",
                "footer",
                "aside",
                "nav",
                "img",
            ]
        ):
            tag.extract()

        # Get the header content
        title_content = soup.find("h1")
        title_text = title_content.get_text() if title_content else ""

        # Get Sub Heading
        subtitle_content = soup.find("h2")
        subtitle_text = subtitle_content.get_text() if subtitle_content else ""

        # Get the paragraph content
        paragraph_content = soup.find_all("p")
        paragraph_text = " ".join([p.get_text() for p in paragraph_content])

        # Combine header and paragraph text
        visible_text = f"{title_text}\n\n{subtitle_text}\n\n{paragraph_text}"

        # Remove multiple whitespaces and newlines
        visible_text = re.sub(r"\s+", " ", visible_text)
        return visible_text.strip()
    except Exception as e:
        print(f"Error occurred while scraping the data: {e}")
        return None


rss_feeds = [
    "https://zeenews.india.com/rss/india-national-news.xml",
    "https://www.aajtak.in/rss/india.xml",
    "https://www.abplive.com/news/india/feed",
    "https://feeds.feedburner.com/ndtvnews-india-news",
    "https://www.indiatoday.in/rss/1206514",
    "https://indianexpress.com/section/india/feed/",
]

while True:
    # Create an empty list to store data for each iteration
    data = []

    try:
        # Iterate through each RSS feed
        for rss_feed in rss_feeds:
            feed = parse(rss_feed)

            # Print feed information for debugging
            print(f"Feed: {rss_feed}")
            print(f"Number of entries: {len(feed.entries)}")

            # Iterate through entries and extract information
            for entry in feed.entries:
                title = entry.title
                link = entry.link
                published = entry.published
                author_info = entry.get("author_detail", {}).get("name", "N/A")

                # Call the scrape_website function to get content
                scraped_data = scrape_website(link)

                data.append([title, link, published, author_info, scraped_data])

        # Create a DataFrame from the collected data
        columns = ["Title", "Link", "Published", "Author Info", "Content"]
        df = pd.DataFrame(data, columns=columns)

        # Save the DataFrame to a CSV file
        df.to_csv("output_data.csv", index=False)

        # Print a message to indicate the iteration is complete
        print("Iteration complete. Waiting for the next iteration...")

    except Exception as e:
        print(f"Error occurred: {e}")

    # Sleep for a specific duration (e.g., 1 hour) before the next iteration
    time.sleep(3600)  # Sleep for 1 hour (3600 seconds)
