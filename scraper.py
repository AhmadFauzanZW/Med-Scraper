from bs4 import BeautifulSoup
import requests
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


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
    company_names3 = []
    phone_numbers3 = []
    links3 = []

    print("Opening the Chrome browser...")

    chrome_driver_path = "C:/Python/Project/chromedriver-win64/chromedriver.exe"

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    driver.get(url)
    time.sleep(3)

    driver.find_element(by=By.XPATH, value="/html/body/form/div[4]/div[3]/div/a[4]").click()
    time.sleep(3)

    country_select = driver.find_element(By.XPATH, "/html/body/form/div[4]/div[8]/div[2]/select")
    drop = Select(country_select)

    option = country_select.find_elements(By.TAG_NAME, 'option')
    option = len(option)

    drop.select_by_index(1)
    time.sleep(1)

    for i in range(option):
        drop.select_by_index(i)
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, 'html5lib')

        table = soup.find('table', class_='table_2')
        # print(table)

        rows = table.find_all('tr')[1:]
        # print(rows)

        for i in rows:
            data = i.find('a')
            company_name = data.text.strip()
            link = data.get('href')

            phone_number = i.find_all('td')[1].text.strip()

            company_names3.append(company_name)
            phone_numbers3.append(phone_number)
            links3.append(link)

            print(company_name)
            print(link)
            print(phone_number)

        print(company_names3)
        print(phone_numbers3)
        print(links3)

    return company_names3, phone_numbers3, links3