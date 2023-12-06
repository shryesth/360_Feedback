from autoscraper import AutoScraper
import pandas as pd

#scraping books URL

TravelCategoryLink = 'https://books.toscrape.com/catalogue/category/books/travel_2/index.html'
WantedList=["https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"]
BooksUrlScraper = AutoScraper()
BooksUrlScraper.build(TravelCategoryLink, wanted_list=WantedList)

#scraping Book Info
BookPageUrl = "https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html" 
WantedList=["It's Only the Himalayas", "£45.17"]
BookInfoScraper = AutoScraper()
BookInfoScraper.build(BookPageUrl, wanted_list=WantedList)

#Scraping info of each book and storing into an excel file
BooksUrlList = BooksUrlScraper.get_result_similar(TravelCategoryLink) 
BooksInfoList = []
for Url in BooksUrlList:
        book_info = BookInfoScraper.get_result_exact(Url)
        BooksInfoList.append(book_info)

df = pd.DataFrame(BooksInfoList, columns =["Book Title", "Price"])
# df.to_excel("BooksInTravelCategory.xlsx")
print(df)

# BookInfoScraper.save('bookinfoscraper')

# SavedScraper = AutoScraper()
# SavedScraper.load('bookinfoscraper')