from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.chemnet.com/Products/supplier.cgi?f=plist;terms=15356-60-2;submit=search"

r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, 'html5lib')
# print(soup)

box = soup.find('div', class_ = "wrapper search-result")
# print(box)

table = box.find('tbody')
# print(table)

datas = table.find_all('td')
# print(datas)

Datas = []

for i in datas:
    data = i.text.strip()
    Datas.append(data)
Company = Datas[0::2]
Ph_num = Datas[1::2]
# print(Company)
# print(Ph_num)

links = table.find_all('a')

Links = []

for i in links:
    link = i.get('href')
    Links.append(link)
# print(Links)

combined = list(zip(Ph_num, Links))
Company_Details = [list(pair) for pair in combined]
# print(Company_Details)

Suppliers = dict(zip(Company, Company_Details))
print(Suppliers)

table_data = {
    'Company': Company,
    'Phone Number': Ph_num,
    'Link': Links
}

df = pd.DataFrame(table_data)
print(df)

# df.to_excel("suppliers.xlsx", index=False)

