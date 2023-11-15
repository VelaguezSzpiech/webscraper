# Code README

## Web Scraping Documentation

These scripts are designed to extract information from a web page and its linked pages using Python. The primary purpose is to demonstrate web scraping using the `requests` library for initial page retrieval, `BeautifulSoup` for HTML parsing, and optionally `Selenium` for interacting with dynamic content.

### Requirements
- Python 3.x
- [requests](https://docs.python-requests.org/en/master/) library
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) library
- [Selenium](https://www.selenium.dev/documentation/en/) library (optional, required only for the first script)

### Installation

Ensure you have the required libraries installed using the following:

```bash
pip install requests beautifulsoup4 selenium
```

Note: For the first script, you also need to download the [ChromeDriver](https://sites.google.com/chromium.org/driver/) executable and add it to your system's PATH.

### Usage

#### Script 1: Using Selenium for Dynamic Content

```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver

def extract_job_information(url):
    # ... (same code as provided)

# Example usage with a documentation URL
docs_url = "https://microsoft.github.io/autogen/docs/Getting-Started"
result = extract_job_information(docs_url)
save_to_file(result, 'output.txt', words_per_line=5)
```

This script utilizes `Selenium` to click on links and read through the pages. Make sure you have the `ChromeDriver` executable in your PATH.

#### Script 2: Standard Web Scraping

```python
import requests
from bs4 import BeautifulSoup

def extract_job_information(url):
    # ... (same code as provided)

# Example usage with a documentation URL
docs_url = "https://microsoft.github.io/autogen/docs/Getting-Started"
result = extract_job_information(docs_url)

# Save the result to a file with line breaks every 5 words
save_to_file(result, 'output.txt', words_per_line=5)
```

This script performs standard web scraping without using `Selenium`. It extracts information from the main page and linked pages.

### Functionality

Both scripts follow a similar structure:

1. **Page Retrieval**: Send a GET request to the specified URL using the `requests` library.

2. **HTML Parsing**: Use `BeautifulSoup` to parse the HTML content of the page.

3. **Information Extraction**: Extract relevant information based on the HTML structure. For example, finding a specific div or all links with a particular class.

4. **Optional Selenium Interaction (Script 1)**: If using `Selenium`, click on links and read through the pages to extract additional information.

5. **Result Formatting and Saving**: Format the extracted information and save it to a file with specified line breaks.

### Customization

Feel free to customize the code based on the structure of the web pages you are working with. Adjust the HTML tags and classes used for extraction according to the target website's structure.

### Note

- Ensure that you comply with the terms of service of the website you are scraping.
- Web scraping may be subject to legal and ethical considerations. Always check and respect the website's terms of service.

### License

This code is provided under the [MIT License](LICENSE). Feel free to modify and use it according to your needs.

---

**Author:** Velaguez
**Date:** 15/11/2023
