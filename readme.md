# Python Web Scraper

This is a Python script that scrapes information from a web page and its linked pages using requests, BeautifulSoup, and Selenium. It also caches the results to avoid unnecessary requests.

## Requirements

- Python 3.9
- requests
- BeautifulSoup
- Selenium
- ChromeDriver

## Installation

- Install the required libraries using `pip install requests beautifulsoup4 selenium`
- Download the ChromeDriver executable from https://chromedriver.chromium.org/ and add it to your system's PATH

## Usage

- Run the script with `python webscraper.py`
- Specify the URL of the web page you want to scrape as `docs_url`
- Specify the directory where you want to save the output file as `save_directory`
- The script will extract the text from the main page and the linked pages, and save it as a JSON file in the output directory
- The script will also create a cache folder and store the results with a hash of the URL as the filename
- If the cache file exists and is valid, the script will use the cached result instead of scraping the web page again

## License

All rights reserved. This software and related documentation are the property of Velaguez Szpiech, and are protected under applicable intellectual property laws. You may not use, modify, reproduce, distribute, or sell this software without explicit permission from the owner. For any inquiries, please contact velaguez1@gmail.com.
