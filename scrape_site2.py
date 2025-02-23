import time
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd

url = "https://www.chemicalbook.com/ChemicalProductProperty_DE_CB4116411.htm"

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

# for i in range(option):
#     drop.select_by_index(i)
#     time.sleep(2)
#
#     soup = BeautifulSoup(driver.page_source, 'html5lib')
#
#     table = soup.find('table', class_ = 'table_2')
#     # print(table)
#
#     rows = table.find_all('tr')[1:]
#     # print(rows)
#
#     for i in rows:
#         data = i.find('a')
#         company_name = data.text.strip()
#         link = data.get('href')
#
#         phone_numbers = table.find_all('td')
#         phone_number = phone_numbers[1].text.strip()
#
#         company_names3.append(company_name)
#         phone_numbers3.append(phone_number)
#         links3.append(link)
#
#         print(company_name)
#         print(link)
#         print(phone_number)
#
#     print(company_names3)
#     print(phone_numbers3)
#     print(links3)
#
# Datas = {
#     'Company':company_names3,
#     'Phone Number':phone_numbers3,
#     'Link':links3
# }
#
# df = pd.DataFrame(Datas)
# print(df)


drop.select_by_index(3)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html5lib')

table = soup.find('table', class_ = 'table_2')
# print(table)

rows = table.find_all('tr')[1:]
# print(rows)

for i in rows:
    print(i.text.strip())
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
