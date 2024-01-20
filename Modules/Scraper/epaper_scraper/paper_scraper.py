import requests
from bs4 import BeautifulSoup
import os
import os.path
from datetime import date, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

NEWSPAPERS = [
    {
        "name": "Economic_times",
        "url": "https://www.dailyepaper.in/economic-times-newspaper-today/",
    },
    {
        "name": "Times_of_India",
        "url": "https://www.dailyepaper.in/times-of-india-epaper-pdf-download-2023/",
    },
    # ... add other newspapers
]


def is_downloadable(url: str) -> bool:
    response = requests.head(url, allow_redirects=True)
    content_type = response.headers.get("content-type", "").lower()
    return not ("text" in content_type or "html" in content_type)


def get_newspaper_links(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.content, "html.parser")
    return [
        tag.get("href", "")
        for tag in soup("a")
        if "https://vk.com/" in tag.get("href", "")
    ]


def download_pdf_with_button_click(link, filename, target_directory):
    # Set download preferences to force external download
    chrome_options = webdriver.ChromeOptions()
    prefs = {
        "plugins.always_open_pdf_externally": True,
        "download.default_directory": target_directory,  # Set the download directory
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # chrome_options.add_argument("--headless")
    # # Ignore SSL errors
    # chrome_options.add_argument("--ignore-certificate-errors")

    # Initialize a browser with the specified options
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the link
        driver.get(link)

        # Find the download button by class name and text content
        button_xpath = "//button[contains(@class, 'FlatButton') and contains(@class, 'FlatButton--primary') and contains(@class, 'FlatButton--size-m') and .//span[contains(@class, 'FlatButton__content') and text()='Download file']]"
        download_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, button_xpath))
        )

        # Record the start time for download
        start_time = time.time()

        # Click the button
        download_button.click()

        # Poll for the completion of the download
        max_poll_attempts = 60  # Maximum attempts to check for the file
        poll_interval = 1  # Time interval between polling attempts

        for _ in range(max_poll_attempts):
            files = [
                file
                for file in os.listdir(target_directory)
                if file.endswith((".pdf", ".crdownload"))
            ]
            if any(file.endswith(".pdf") for file in files):
                # Get the name of the downloaded file
                downloaded_file = [file for file in files if file.endswith(".pdf")][0]
                # Rename the downloaded file
                os.rename(
                    os.path.join(target_directory, downloaded_file),
                    os.path.join(target_directory, filename),
                )
                print(f"Done downloading: {filename}")
                break
            elif any(file.endswith(".crdownload") for file in files):
                print("Download in progress. Waiting for completion...")
            else:
                print("No download file detected.")
            time.sleep(poll_interval)
        else:
            print(f"Timeout: Download may not have completed in time.")

        # Record the end time for download
        end_time = time.time()
        print(f"Time taken for download: {end_time - start_time} seconds")

    except Exception as e:
        print(f"Error during download: {e}")

    finally:
        # Close the browser
        driver.quit()


def main():
    today = date.today()

    print(
        "The following Newspapers are available for download. Select any of them by giving number inputs - "
    )
    for counter, newspaper in enumerate(NEWSPAPERS, start=1):
        print(f'{counter}. {newspaper["name"]}')

    selected_numbers = input("Enter the number for newspapers (separated by space) - ")
    for_how_many_days = int(input("For how many days do you need the papers? "))

    for index in selected_numbers.split():
        newspaper_number = int(index)
        if 1 <= newspaper_number <= len(NEWSPAPERS):
            newspaper_detail = NEWSPAPERS[newspaper_number - 1]
            links = get_newspaper_links(newspaper_detail["url"])

            target_directory = os.path.join(os.getcwd(), newspaper_detail["name"])
            try:
                os.mkdir(target_directory)
            except OSError:
                pass

            for i in range(for_how_many_days):
                if i < len(links):
                    url = links[i]
                    date_that_day = today - timedelta(days=i)

                    if is_downloadable(url):
                        print(
                            f'Downloading {newspaper_detail["name"]} for {date_that_day}...'
                        )
                        download_pdf_with_button_click(
                            url,
                            f"{newspaper_detail['name']}_{date_that_day}.pdf",
                            target_directory,
                        )
                        print("Done :)")
                    else:
                        print(
                            f'{newspaper_detail["name"]} paper not available for {date_that_day}'
                        )
                else:
                    print(
                        f'No link available for {newspaper_detail["name"]} on day {i + 1}'
                    )

        else:
            print(f"Invalid newspaper number: {newspaper_number}")


if __name__ == "__main__":
    main()
