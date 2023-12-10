import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all h1, h2, and p tags
        h1_tags = [tag.text.strip() for tag in soup.find_all('h1')]
        h2_tags = [tag.text.strip() for tag in soup.find_all('h2')]
        p_tags = [tag.text.strip() for tag in soup.find_all('p')]

        # Combine the results into a dictionary
        result = {
            'h1': h1_tags[0],
            'h2': h2_tags[0],
            'p': ' '.join(p_tags)
        }

        return result

    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch content from {url}. Status code: {response.status_code}")
        return None

# Example usage:
url_to_scrape = "https://www.indiatoday.in/magazine/nation/story/20230717-shifting-to-election-gear-baghel-blows-the-bugle-2403446-2023-07-07?utm_source=rss"
scraped_data = scrape_website(url_to_scrape)

if scraped_data:
    print("H1 Tags:")
    print(scraped_data['h1'])

    print("\nH2 Tags:")
    print(scraped_data['h2'])

    print("\nParagraphs:")
    print(scraped_data['p'])
