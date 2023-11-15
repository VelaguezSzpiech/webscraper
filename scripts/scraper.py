import requests
from bs4 import BeautifulSoup

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
        otherpages_text = ', '.join([page.get_text(strip=True) for page in otherpages])

        return f"Main Page: {mainpage}\nOther Pages: {otherpages_text}"
    else:
        return "Failed to retrieve the webpage."

def save_to_file(data, filename='output.txt', words_per_line=5):
    words = data.split()
    formatted_text = '\n'.join(' '.join(words[i:i+words_per_line]) for i in range(0, len(words), words_per_line))
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(formatted_text)


# Example usage with a documentation URL
docs_url = "https://microsoft.github.io/autogen/docs/Getting-Started"
result = extract_job_information(docs_url)

# Save the result to a file with line breaks every 5 words
save_to_file(result, 'output.txt', words_per_line=5)
