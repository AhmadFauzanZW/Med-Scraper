import os

import pandas as pd

def create_dataframe(companies, phone_numbers, links, start_index=1):
    """Create pandas DataFrame from company data."""
    table_data = {
        'Company': companies,
        'Phone Number': phone_numbers,
        'Link': links
    }
    df = pd.DataFrame(table_data)
    # Set the index name to avoid 'Unnamed' column
    df.index = range(start_index, start_index + len(companies))
    df.index.name = 'Index'
    return df

def save_or_append_to_excel(df, filename):
    """Save DataFrame to Excel file or append to existing file."""
    if os.path.exists(filename):
        # Read existing file
        existing_df = pd.read_excel(filename, index_col='Index')
        # Combine existing and new data
        combined_df = pd.concat([existing_df, df])
        # Ensure index is continuous
        combined_df.index = range(1, len(combined_df) + 1)
        combined_df.index.name = 'Index'
        # Save combined data
        combined_df.to_excel(filename)
    else:
        # If file doesn't exist, create new
        df.to_excel(filename)