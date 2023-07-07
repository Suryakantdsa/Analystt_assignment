import requests
from bs4 import BeautifulSoup


def scrape_product(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    description_element = soup.find('div', {'id': 'productDescription'})
    description = description_element.text.strip() if description_element else 'N/A'

    asin_element = soup.find('th', text='ASIN')
    asin = asin_element.find_next('td').text.strip() if asin_element else 'N/A'

    product_description_element = soup.find(
        'div', {'id': 'productDescription'})
    product_description = product_description_element.text.strip(
    ) if product_description_element else 'N/A'

    manufacturer_element = soup.find('a', {'id': 'bylineInfo'})
    manufacturer = manufacturer_element.text.strip() if manufacturer_element else 'N/A'

    print('Product URL:', url)
    print('Description:', description)
    print('ASIN:', asin)
    print('Product Description:', product_description)
    print('Manufacturer:', manufacturer)
    print('--------------------')


def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all('div', {'data-component-type': 's-search-result'})

    for product in products:
        productUrl = 'https://www.amazon.in' + product.find('a', {'class': 'a-link-normal s-no-outline'})['href']
        scrape_product(productUrl)
        print('Product URL:', productUrl)


base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_'
num_pages = 20

for page in range(1, num_pages + 1):
    url = base_url + str(page)
    print('Scraping page', page)
    scrape_page(url)
