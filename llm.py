from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLDatabase.from_uri("postgresql://postgres:1234@localhost:5432/bytegenie")

llm = ChatOpenAI(openai_api_key=os.getenv("OPEN_AI_KEY"), model="gpt-3.5-turbo", temperature=0)
agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)
chain = create_sql_query_chain(llm, db)

examples = [
    {
      "natural_language_query": "Give emails of people working in health industry",
      "sql_query": '''"SELECT first_name, last_name, email FROM people_info
        JOIN company_info ON people_info.homepage_base_url = company_info.homepage_base_url
        JOIN event_info ON company_info.event_url = event_info.event_url
        WHERE event_info.mapped_industry ILIKE '%health%';
      '''
    },
    {
      "natural_language_query": "Give email of people working in finance industry",
      "sql_query": '''"SELECT first_name, last_name, email FROM people_info
        JOIN company_info ON people_info.homepage_base_url = company_info.homepage_base_url
        WHERE company_info.mapped_industry ILIKE '%finance%';
      '''
    },
    {
      "natural_language_query": "Find sales people for companies that are attending events in Singapore over the next 9 months",
      "sql_query": '''"SELECT first_name, last_name, job_title, email
        FROM people_info
        JOIN company_info ON people_info.homepage_base_url = company_info.homepage_base_url
        JOIN event_info ON company_info.event_url = event_info.event_url
        WHERE event_info.event_country = 'Singapore'
        AND event_info.event_start_date BETWEEN CURRENT_DATE AND CURRENT_DATE + INTERVAL '9 months'
        AND job_title ILIKE '%sales%';"
      '''
    },
    {
      "natural_language_query": "Find me events that companies in Pharmaceuticals sector are attending",
      "sql_query": '''
        SELECT company_name, event_info.event_name, event_info.event_venue, 
        event_info.event_country, event_info.event_start_date, 
        event_info.event_end_date, event_info.event_description, event_info.event_url
        FROM event_info JOIN company_info ON company_info.event_url = event_info.event_url
        WHERE company_info.mapped_industry ILIKE '%pharmaceuticals%';
      '''
    },
    {
      "natural_language_query": "check for event in tech industry",
      "sql_query": '''
        SELECT event_info.event_name, event_info.event_venue, event_info.event_country, event_info.event_start_date, 
        event_info.event_end_date, event_info.event_description, event_info.event_url
        FROM event_info WHERE company_info.mapped_industry ILIKE '%event_info%';
      '''
    },
]

def format_prompt_with_examples(natural_language_query):
    prompt = "You are a helpful database assistant. Use the following database schema when creating your answers:\n"
    prompt += "Don't respond to unrelated questions with respect to the database, tell user if its an unrelated question\n"
    prompt += "Tables: people_info, company_info, event_info\n"
    prompt += "event_info columns: event_logo_url, event_name, event_start_date, event_end_date, event_venue, event_country, event_description, url, mapped_industry\n"
    prompt += "people_info columns: first_name, middle_name, last_name, job_title, person_city, person_state, person_country, email_pattern, homepage_base_url, duration_in_current_job, duration_in_current_company, email\n"
    prompt += "company_info columns: mapped_industry, company_logo_url, company_logo_text, company_name, relation_to_event, event_url, company_revenue, n_employees, company_phone, company_founding_year, company_address, company_industry, company_overview, homepage_url, linkedin_company_url, homepage_base_url, company_logo_url_on_event_page, company_logo_match_flag\n"
    prompt += "Always add table prefixes if you are using joins, eg company_info.event_url, company_info.company_name, event_info.event_name, event_info.event_venue, people.person_city etc\n"
    for example in examples:
        prompt += f"Natural Language Query: {example['natural_language_query']}\n"
        prompt += f"SQL Query: {example['sql_query']}\n\n"
    
    prompt += "Don't put any limits, return all of the data\n"
    prompt += "You will need to join people_info and company_info on people_info.home_base_url and company_info.home_base_url. Also, do same for company_info.event_url and event_info.url"
    prompt += f"Natural Language Query: {natural_language_query}\n"
    prompt += "SQL Query:"

    return prompt

agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True,
    agent_type= "openai-tools",
    return_intermediate_steps=True
)

def convert_to_sql(natural_language_query):
    # Generate the SQL query using the agent executor
    # response = agent_executor.invoke(natural_language_query)
    response = chain.invoke({"question": format_prompt_with_examples(natural_language_query)})

    print("tahamazari ",response)
    
    # Remove markdown syntax if present
    sql_query = response.strip("```")

    print("Generated SQL Query:", sql_query)
    return sql_query