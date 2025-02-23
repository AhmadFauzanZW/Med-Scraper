# scraper.py
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


def fetch_webpage(url):
    """Fetch webpage content and return BeautifulSoup object."""
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html5lib')


def extract_table_data_site1(soup):
    """Extract table data from the first website (chemnet)."""
    box = soup.find('div', class_="wrapper search-result")
    if not box:
        return None
    return box.find('tbody')


def extract_company_data_site1(table):
    """Extract company names and phone numbers from first website."""
    if not table:
        return [], []

    datas = table.find_all('td')
    all_data = [i.text.strip() for i in datas]

    company_names = all_data[0::2]
    phone_numbers = all_data[1::2]
    return company_names, phone_numbers


def extract_links_site1(table):
    """Extract links from first website."""
    if not table:
        return []

    links = table.find_all('a')
    return [link.get('href') for link in links]


def scrape_site2(url):
    """
    Scrape data from the second website.
    Replace this with actual scraping logic for your second website.
    """
    soup = fetch_webpage(url)
    # Add your scraping logic here for the second website
    # This is just a placeholder example
    companies = []
    phone_numbers = []
    links = []

    # Example scraping logic (modify according to the second website's structure):
    # boxes = soup.find_all('div', class_='company-box')
    # for box in boxes:
    #     companies.append(box.find('h2').text.strip())
    #     phone_numbers.append(box.find('span', class_='phone').text.strip())
    #     links.append(box.find('a')['href'])

    return companies, phone_numbers, links


# data_processor.py
def create_company_details(phone_numbers, links):
    """Create combined list of company details."""
    combined = list(zip(phone_numbers, links))
    return [list(pair) for pair in combined]


def create_suppliers_dict(companies, company_details):
    """Create dictionary mapping companies to their details."""
    return dict(zip(companies, company_details))


def create_dataframe(companies, phone_numbers, links, start_index=1):
    """Create pandas DataFrame from company data."""
    table_data = {
        'Company': companies,
        'Phone Number': phone_numbers,
        'Link': links
    }
    return pd.DataFrame(table_data, index=range(start_index, start_index + len(companies)))


def save_or_append_to_excel(df, filename):
    """Save DataFrame to Excel file or append to existing file."""
    if os.path.exists(filename):
        # Read existing file
        existing_df = pd.read_excel(filename)
        # Combine existing and new data
        combined_df = pd.concat([existing_df, df], ignore_index=False)
        # Save combined data
        combined_df.to_excel(filename)
    else:
        # If file doesn't exist, create new
        df.to_excel(filename)


# main.py
from scraper import (
    fetch_webpage,
    extract_table_data_site1,
    extract_company_data_site1,
    extract_links_site1,
    scrape_site2
)
from data_processor import (
    create_company_details,
    create_suppliers_dict,
    create_dataframe,
    save_or_append_to_excel
)


def scrape_site1(url):
    """Scrape data from the first website (chemnet)."""
    soup = fetch_webpage(url)
    table = extract_table_data_site1(soup)
    companies, phone_numbers = extract_company_data_site1(table)
    links = extract_links_site1(table)
    return companies, phone_numbers, links


def main():
    # URLs for scraping
    url1 = "https://www.chemnet.com/Products/supplier.cgi?f=plist;terms=15356-60-2;submit=search"
    url2 = "YOUR_SECOND_WEBSITE_URL_HERE"  # Replace with your second website URL
    output_file = "suppliers.xlsx"

    # Scrape first website
    print("Scraping first website...")
    companies1, phone_numbers1, links1 = scrape_site1(url1)
    df1 = create_dataframe(companies1, phone_numbers1, links1)
    save_or_append_to_excel(df1, output_file)

    # Scrape second website
    print("Scraping second website...")
    companies2, phone_numbers2, links2 = scrape_site2(url2)
    if companies2:  # Only process if data was found
        # Create DataFrame with index continuing from the end of first DataFrame
        start_index = len(companies1) + 1
        df2 = create_dataframe(companies2, phone_numbers2, links2, start_index)
        save_or_append_to_excel(df2, output_file)

    # Print final results
    final_df = pd.read_excel(output_file)
    print("\nFinal Combined DataFrame:")
    print(final_df)


if __name__ == "__main__":
    main()