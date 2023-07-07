import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all('div', {'data-component-type': 's-search-result'})

    for product in products:
        productUrl = product.find(
            'a', {'class': 'a-link-normal s-no-outline'})['href']
        productName = product.find(
            'span', {'class': 'a-size-medium a-color-base a-text-normal'}).text
        productPrice = product.find('span', {'class': 'a-offscreen'}).text
        rating = product.find('span', {'class': 'a-icon-alt'}).text
        noOfReview = product.find('span', {'class': 'a-size-base'}).text

        print('Product URL:', productUrl)
        print('Product Name:', productName)
        print('Product Price:', productPrice)
        print('Rating:', rating)
        print('Number of Reviews:', noOfReview)
        print('---------Next product page-----------')


base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_'
num_pages = 20

for page in range(1, num_pages + 1):
    url = base_url + str(page)
    print('Scraping page', page)
    scrape_page(url)
