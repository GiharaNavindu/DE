import requests
from bs4 import BeautifulSoup

def scrape_books(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    books = []
    for book in soup.find_all('h3'):
        books.append(book.a['title'])

    return {"books": books}
