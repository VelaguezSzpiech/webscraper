import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver

def extract_job_information(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant information based on the HTML structure
        mainpage = soup.find('div', class_="container").get_text(strip=True)
        otherpages = soup.find_all('a', class_="menu__link")
        
        # Using Selenium to click on links and read through the pages
        driver = webdriver.Chrome()  # Make sure you have the ChromeDriver executable in your PATH
        for link in otherpages:
            href = link.get('href')
            if href:
                full_url = urljoin(url, href)
                driver.get(full_url)
                # Extract information from the new page, you may need to modify this part
                page_content = driver.page_source
                # Process the page content as needed
                
        driver.quit()  # Close the browser after processing

        return f"Main Page: {mainpage}\nOther Pages content: Processed with Selenium"
    else:
        return "Failed to retrieve the webpage."

# Example usage with a documentation URL
docs_url = "https://microsoft.github.io/autogen/docs/Getting-Started"
result = extract_job_information(docs_url)
print(result)
