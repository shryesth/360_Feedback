from autoscraper import AutoScraper

url="https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
WantedList=["It's Only the Himalayas", "£45.17"]

scraper = AutoScraper()
scrapedData = scraper.build(url,wanted_list=WantedList)
# print(scrapedData)

another_book_url = "https://books.toscrape.com/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html"
# scraped_data2 = scraper.get_result_similar(another_book_url)
scraped_data2 = scraper.get_result_exact(another_book_url)
print(scraped_data2)