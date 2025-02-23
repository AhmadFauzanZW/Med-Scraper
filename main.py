import pandas as pd

from scraper import (
    # fetch_webpage,
    scrape_site1,
    scrape_site2
)
from data_processor import (
    create_dataframe,
    save_or_append_to_excel
)


def main():
    # URL for scraping
    url1 = "https://www.chemnet.com/Products/supplier.cgi?f=plist;terms=15356-60-2;submit=search"
    url2 = "https://china.chemnet.com/product/search.cgi?type=word&f=plist&terms=15356-60-2"
    # Output file name
    output_file = "suppliers.xlsx"

    # Scrape Website-1 ---------------------------------------------------
    company_names1, phone_numbers1, links1 = scrape_site1(url1)
    # Create and save DataFrame Website-1
    df1 = create_dataframe(company_names1, phone_numbers1, links1)
    save_or_append_to_excel(df1, "suppliers.xlsx")
    # --------------------------------------------------------------------

    # Scrape Website-2 ---------------------------------------------------

    company_names2, phone_numbers2, links2 = scrape_site2(url2)
        # Create and save DataFrame Website-2
    if company_names2:
        start_index = len(company_names1) + 1
        df2 = create_dataframe(company_names2, phone_numbers2, links2, start_index)
        save_or_append_to_excel(df2, "suppliers.xlsx")
        # --------------------------------------------------------------------


    # Print results
    final_df = pd.read_excel(output_file)
    print("\nFinal Combined DataFrame:")
    print(final_df)


if __name__ == "__main__":
    main()