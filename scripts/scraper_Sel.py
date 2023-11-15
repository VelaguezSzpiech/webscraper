import requests
import os
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
import hashlib

CACHE_FOLDER = 'E:\Ai_Systems\pythonwebscraper\cache'

def get_page_content(url):
    response = requests.get(url)
    return response.text if response.status_code == 200 else None

def get_page_hash(content):
    return hashlib.sha256(content.encode()).hexdigest() if content else None

def is_cache_valid(url, cached_hash):
    current_content = get_page_content(url)
    current_hash = get_page_hash(current_content)
    return current_hash == cached_hash

def extract_job_information(url):
    # Create a hash of the URL to use as a filename in the cache
    url_hash = hashlib.sha256(url.encode()).hexdigest()
    cache_filename = os.path.join(CACHE_FOLDER, f"{url_hash}.txt")

    if os.path.exists(cache_filename):
        with open(cache_filename, 'r', encoding='utf-8') as cache_file:
            cached_result = cache_file.read()
            cached_hash = cached_result.split('\n')[0]  # Assume the hash is stored on the first line

            if is_cache_valid(url, cached_hash):
                return cached_result

    # If not cached or cache is invalid, proceed with the web scraping
    current_result = scrape_and_process(url)

    # Save the result to the cache
    with open(cache_filename, 'w', encoding='utf-8') as cache_file:
        cache_file.write(f"{get_page_hash(get_page_content(url))}\n{current_result}")

    return current_result

def scrape_and_process(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        mainpage = soup.find('div', class_="container").get_text(strip=True)
        otherpages = soup.find_all('a', class_="menu__link")

        driver = webdriver.Chrome()
        all_pages_text = []
        for link in otherpages:
            href = link.get('href')  # corrected here
            if href:
                full_url = urljoin(url, href)
                driver.get(full_url)
                page_content = driver.page_source
                page_soup = BeautifulSoup(page_content, 'html.parser')
                page_text = page_soup.get_text(strip=True)
                all_pages_text.append(page_text)

        driver.quit()

        return f"Main Page: {mainpage}\nOther Pages: {all_pages_text}"
    else:
        return "Failed to retrieve the webpage."
# Ensure that the cache folder exists
if not os.path.exists(CACHE_FOLDER):
    os.makedirs(CACHE_FOLDER)
# Ensure that the cache folder exists

def save_to_file(data, filename='output.json', directory='.'):
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Example usage with a documentation URL
docs_url = "https://microsoft.github.io/autogen/docs/Getting-Started"
result = extract_job_information(docs_url)

# Specify the directory where you want to save the file
save_directory = 'E:\\Ai_Systems\\pythonwebscraper\\output'
save_to_file(result, 'output.json', directory=save_directory)
