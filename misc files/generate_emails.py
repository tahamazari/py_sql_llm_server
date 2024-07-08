import pandas as pd

# Load the CSV file
file_path = './people_info.csv'
df = pd.read_csv(file_path)

# Function to generate email based on pattern
def generate_email(row):
    first_name = row['first_name']
    last_name = row['last_name'] if pd.notna(row['last_name']) else ""
    homepage_base_url = row['homepage_base_url']
    pattern = row['email_pattern']
    
    # Ensure necessary fields are present
    if pd.isna(first_name) or pd.isna(homepage_base_url):
        return None
    
    # Use default pattern if no pattern is specified
    if pd.isna(pattern):
        pattern = '[first]'  
    
    # Generate email based on pattern
    email = None
    if pattern == '[first]':
        email = f"{first_name.lower()}@{homepage_base_url}"
    elif pattern == '[last]':
        email = f"{last_name.lower()}@{homepage_base_url}"
    elif pattern == '[first][last]':
        email = f"{first_name.lower()}{last_name.lower()}@{homepage_base_url}"
    elif pattern == '[first].[last]':
        email = f"{first_name.lower()}.{last_name.lower()}@{homepage_base_url}"
    elif pattern == '[first_initial][last]':
        email = f"{first_name[0].lower()}{last_name.lower()}@{homepage_base_url}"
    elif pattern == '[first][last_initial]':
        if len(last_name) > 0:
            email = f"{first_name.lower()}{last_name[0].lower()}@{homepage_base_url}"
        else:
            email = f"{first_name.lower()}@{homepage_base_url}"
    elif pattern == '[first_initial].[last]':
        if len(last_name) > 0:
            email = f"{first_name[0].lower()}.{last_name.lower()}@{homepage_base_url}"
        else:
            email = f"{first_name.lower()}@{homepage_base_url}"
    elif pattern == '[first_initial][last_initial]':
        if len(last_name) > 0:
            email = f"{first_name[0].lower()}{last_name[0].lower()}@{homepage_base_url}"
        else:
            email = f"{first_name.lower()}@{homepage_base_url}"
    elif pattern == '[first_initial][last_initial][company_domain]':
        if len(last_name) > 0:
            email = f"{first_name[0].lower()}{last_name[0].lower()}@{homepage_base_url}"
        else:
            email = f"{first_name.lower()}@{homepage_base_url}"
    else:
        email = f"{first_name.lower()}@{homepage_base_url}"
    
    return email

# Apply the function to each row
df['email'] = df.apply(generate_email, axis=1)

# Save the updated dataframe to a new CSV file
output_file_path = './people_info_with_emails.csv'
df.to_csv(output_file_path, index=False)

print("Emails added and CSV file saved as 'people_info_with_emails.csv'.")
