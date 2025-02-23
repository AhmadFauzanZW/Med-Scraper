from scraper import fetch_webpage

url = "https://china.chemnet.com/product/search.cgi?type=word&f=plist&terms=15356-60-2"

soup = fetch_webpage(url)

box = soup.find('div', class_ = 'sj-list')
# print(box)

datas = box.find_all('td')
all_data = [i.text.strip() for i in datas]
print(all_data)

company_names2 = all_data[0::2]
phone_numbers2 = all_data[1::2]

links = box.find_all('a')
links2 = [link.get('href') for link in links]
print(links2)