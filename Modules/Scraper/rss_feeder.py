from feedparser import parse
import pandas as pd
from autoscraper import AutoScraper


url_zee = "https://zeenews.india.com/rss/india-national-news.xml"
url_aaj_tak = "https://www.aajtak.in/rss/india.xml"
url_toi = "http://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms"
url_abp = "https://www.abplive.com/news/india/feed"

data = []

feed = parse(url_zee)

# print(feed)
# # print(feed['entries'][0])


# Iterate through entries and extract information
for entry in feed.entries:
    title = entry.title
    link = entry.link
    published = entry.published
    author_info = entry.get("author_detail", {}).get("name", "N/A")

    data.append([title, link, published, author_info])

    # # Print or process the extracted information as needed
    # print("Title:", title)
    # print("Link:", link)
    # # print("Summary:", summary)
    # print("Published:", published)
    # print("Author Info:", author_info)
    # print("\n" + "-"*50 + "\n")  # Separating entries for better readability

columns = ["Title", "Link", "Published", "Author Info"]
df = pd.DataFrame(data, columns=columns)

# print(df)

