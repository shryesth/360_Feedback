import requests
from bs4 import BeautifulSoup
import os
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

NEWSPAPERS = [
    {"name": 'Economic_times', 'url': 'https://www.dailyepaper.in/economic-times-newspaper-today/'},
    {"name": 'Times_of_India', 'url': 'https://www.dailyepaper.in/times-of-india-epaper-pdf-download-2023/'},
    # ... add other newspapers
]

def is_downloadable(url: str) -> bool:
    response = requests.head(url, allow_redirects=True)
    content_type = response.headers.get('content-type', '').lower()
    return not ('text' in content_type or 'html' in content_type)

def get_newspaper_links(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.content, 'html.parser')
    return [tag.get('href', '') for tag in soup('a') if 'https://vk.com/' in tag.get('href', '')]

def download_pdf_with_button_click(link, filename):
    # Initialize a browser (you may need to download a suitable driver)
    driver = webdriver.Chrome()

    try:
        # Open the link
        driver.get(link)

        # Find the download button by class name and text content
        button_xpath = "//button[contains(@class, 'FlatButton') and contains(@class, 'FlatButton--primary') and contains(@class, 'FlatButton--size-m') and .//span[contains(@class, 'FlatButton__content') and text()='Download file']]"
        download_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, button_xpath))
        )

        # Click the button
        download_button.click()

        # Wait for the download to complete (adjust the sleep time as needed)
        time.sleep(5)

        # Rename the downloaded file (adjust the filename accordingly)
        os.rename("original_filename.pdf", filename)
        print(f'Done downloading: {filename}')

    finally:
        # Close the browser
        driver.quit()

def main():
    today = date.today()

    print("The following Newspapers are available for download. Select any of them by giving number inputs - ")
    for counter, newspaper in enumerate(NEWSPAPERS, start=1):
        print(f'{counter}. {newspaper["name"]}')

    selected_numbers = input('Enter the number for newspapers (separated by space) - ')
    for_how_many_days = int(input('For how many days do you need the papers? '))

    for index in selected_numbers.split():
        newspaper_number = int(index)
        if 1 <= newspaper_number <= len(NEWSPAPERS):
            newspaper_detail = NEWSPAPERS[newspaper_number - 1]
            links = get_newspaper_links(newspaper_detail['url'])

            directory = newspaper_detail['name']
            parent_dir = os.getcwd()
            path = os.path.join(parent_dir, directory)

            try:
                os.mkdir(path)
            except OSError:
                pass

            os.chdir(path)  # Context manager for changing directory
            for i in range(for_how_many_days):
                if i < len(links):
                    url = links[i]
                    date_that_day = today - timedelta(days=i)

                    if is_downloadable(url):
                        print(f'Downloading {newspaper_detail["name"]} for {date_that_day}...')
                        download_pdf_with_button_click(url, f"{newspaper_detail['name']}_{date_that_day}.pdf")
                        print('Done :)')
                    else:
                        print(f'{newspaper_detail["name"]} paper not available for {date_that_day}')
                else:
                    print(f'No link available for {newspaper_detail["name"]} on day {i + 1}')
            os.chdir('../')  # Return to the parent directory

        else:
            print(f"Invalid newspaper number: {newspaper_number}")

if __name__ == "__main__":
    main()
