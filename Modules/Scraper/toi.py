import requests
from bs4 import BeautifulSoup

def scrape_content_from_url(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        # Send a GET request to the URL
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")

            # Find the specific div element using its class
            news_div = soup.find("div", class_="_s30J clearfix")

            # Check if the div is found
            if news_div:
                # Extract the text content from the div
                news_text = news_div.get_text(strip=True)
                return news_text
            else:
                return "Couldn't find the specified div element."
        else:
            return f"Failed to retrieve the page. Status code: {response.status_code}"
    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    # Example usage
    url = "https://timesofindia.indiatimes.com/city/delhi/day-after-lg-recalls-files-kailash-gahlot-loses-law-portfolio-atishi-given-charge/articleshow/105846220.cms"
    content = scrape_content_from_url(url)

    print(content)
