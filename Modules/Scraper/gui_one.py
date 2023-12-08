import streamlit as st
import requests
from bs4 import BeautifulSoup
import re


# Function to scrape only visible text from the given URL
def scrape_visible_text_from_url(url):
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
        st.error(f"Error occurred while scraping the data: {e}")
        return None


# Streamlit UI
def main():
    st.title("Web Data Scraper")

    # Get the URL from the user
    url_input = st.text_input("Enter the URL of the web page:", "")

    if st.button("Scrape Visible Text"):
        if url_input:
            # Extract visible text from the URL
            data = scrape_visible_text_from_url(url_input)
            if data:
                st.success("Visible text successfully scraped!")
                st.subheader("Scraped Text:")
                st.write(data)
            else:
                st.warning("Failed to scrape visible text from the URL.")
        else:
            st.warning("Please enter a valid URL.")


if __name__ == "__main__":
    main()
