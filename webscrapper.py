import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all the article titles and links
        articles = soup.find_all('a', class_='article-link')  # Replace 'article-link' with the actual class or tag used
        
        # Create a structured form to store the extracted information
        extracted_data = []
        for article in articles:
            title = article.text.strip()
            link = article['href']
            extracted_data.append({'title': title, 'link': link})
        
        return extracted_data
    else:
        print('Failed to retrieve the webpage')
        return None

# Example usage
url_to_scrape = 'https://example.com/news'  # Replace with the URL of the website you want to scrape
data = scrape_website(url_to_scrape)

if data:
    for article in data:
        print(f"Title: {article['title']}")
        print(f"Link: {article['link']}")
        print()

        
