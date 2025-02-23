from bs4 import BeautifulSoup
import requests
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service


def fetch_webpage(url):
    """Fetch webpage content and return BeautifulSoup object."""
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html5lib')

def scrape_site1(url):
    # Make a request to URL and initialize BeautifulSoup
    soup = fetch_webpage(url)

    # Find main box/canvas to scrape
    box = soup.find('div', class_="wrapper search-result")
    if not box:
        return None

    # Find main table to scrape
    table = box.find('tbody')
    if not table:
        return [], []

    # Find the needed datas to scrape
    datas = table.find_all('td')
    all_data = [i.text.strip() for i in datas]
    company_names1 = all_data[0::2]
    phone_numbers1 = all_data[1::2]

    if not table:
        return []
    links = table.find_all('a')
    links1 = [link.get('href') for link in links]

    return  company_names1, phone_numbers1, links1

def scrape_site2(url):
    soup = fetch_webpage(url)

    box = soup.find('div', class_ = 'sj-list')
    if not box:
        return None

    table = box.find('tbody')
    if not table:
        return [], []

    datas = table.find_all('td')
    all_data = [i.text.strip() for i in datas]
    company_names2 = all_data[0::2]
    phone_numbers2 = all_data[1::2]

    if not table:
        return []
    links = table.find_all('a')
    links2 = [link.get('href') for link in links]

    return company_names2, phone_numbers2, links2

def scrape_site3(url):
    print("Opening the Chrome browser...")

    chrome_driver_path = "C:/Python/Project/chromedriver-win64/chromedriver.exe"

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    driver.get(url)