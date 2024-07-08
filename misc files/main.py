import pandas as pd
from sqlalchemy import create_engine, Table, Column, Text, Integer, MetaData

# Define the database connection string
db_string = "postgresql://postgres:1234@localhost:5432/bytegenie"

# Create the database engine
engine = create_engine(db_string)

# Create metadata instance
metadata = MetaData()

# Function to read CSV and create table
def create_and_insert_table(csv_path, table_name, columns):
    # Read CSV file into DataFrame
    df = pd.read_csv(csv_path)
    
    # Ensure DataFrame columns match SQL table columns
    df.columns = columns
    
    # Define the table structure
    table = Table(table_name, metadata, *[
        Column(col, Text) for col in columns
    ])
    
    # Create the table in the database
    metadata.create_all(engine)
    
    # Insert data into the table
    df.to_sql(table_name, engine, if_exists='replace', index=False)

# Event Info
event_info_columns = ['event_logo_url', 'event_name', 'event_start_date', 'event_end_date', 'event_venue', 'event_country', 'event_description', 'event_url']
create_and_insert_table('./data/event_info.csv', 'event_info', event_info_columns)

# People Info
people_info_columns = ['first_name', 'middle_name', 'last_name', 'job_title', 'person_city', 'person_state', 'person_country', 'email_pattern', 'homepage_base_url', 'duration_in_current_job', 'duration_in_current_company']
create_and_insert_table('./data/people_info.csv', 'people_info', people_info_columns)

# Company Info
company_info_columns = ['company_logo_url', 'company_logo_text', 'company_name', 'relation_to_event', 'event_url', 'company_revenue', 'n_employees', 'company_phone', 'company_founding_year', 'company_address', 'company_industry', 'company_overview', 'homepage_url', 'linkedin_company_url', 'homepage_base_url', 'company_logo_url_on_event_page', 'company_logo_match_flag']
create_and_insert_table('./data/company_info.csv', 'company_info', company_info_columns)
