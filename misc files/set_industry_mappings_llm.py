from openai import OpenAI
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

industries = [
    ["tech","it","technology","technology services","information technology","software development","IT consulting","IT services","cybersecurity","cloud computing","data analytics","AI","artificial intelligence","machine learning","network security","computer networks"],
    ["finance","banking","financial","investment","insurance","wealth management","asset management","financial planning","fintech","financial technology","Financial Services","venture","capital","venture capital","equity"],
    ["maritime","transportation","shipping","logistics","freight","ocean transport","sea transport"],
    ["staffing","recruiting","recruitment","hiring","talent acquisition","HR services","human resources","employment services"],
    ["health","medical","hospital","clinic","healthcare","patient care","medical services","pharmaceutical","biomedical","biotech","biotechnology","life sciences"],
    ["manufacturing","production","factory","industrial","manufacturing plant","assembly line","mass production"],
    ["retail","shopping","online shopping","ecommerce","store","online store","consumer goods","retail sales","cosmetics"],
    ["education","school","university","college","learning","online education","e-learning","educational services"],
    ["construction","building","contractor","infrastructure","civil engineering","construction services","real estate development"],
    ["consulting","advisory","consultant","business consulting","management consulting","strategy consulting","professional services"],
    ["real estate","property","housing","realty","real estate services","property management","real estate investment","commercial real estate"],
    ["telecommunications","telecom","communication","network","wireless","broadband","internet services","mobile services"],
    ["energy","oil","gas","renewable","power","electricity","solar energy","wind energy","energy services","energy production"],
    ["automotive","car","vehicle","auto","automobile","car manufacturing","vehicle production","auto services"],
    ["food","beverage","restaurant","cafe","drink","food services","hospitality","catering","food production","beverage production"],
    ["entertainment","media","film","music","theater","broadcasting","publishing","content production","multimedia"],
    ["nonprofit","non-profit","charity","ngo","non-governmental organization","social services","philanthropy","volunteer services"],
    ["government","public sector","municipal","state","federal","public administration","government services","public policy"],
    ["agriculture","farming","crop","agro","agribusiness","agricultural production","livestock","dairy farming"],
    ["pharmaceuticals","drug","medicine","biotech","biotechnology","pharmaceutical","pharmaceutical services","drug development","clinical trials","healthcare products","Pharmaceutical Manufacturing","Pharmaceuticals Manufacturing"],
    ["aerospace","aviation","aircraft","space","defense","aerospace engineering","aerospace manufacturing","space exploration"],
    ["hospitality","hotel","resort","travel","tourism","lodging","accommodation services","hospitality management"],
    ["transportation","logistics","freight","delivery","shipping","transport services","cargo","supply chain"],
    ["legal services","law","law firm","attorney","legal consulting","litigation","legal advice","corporate law"],
    ["media","communications","public relations","advertising","marketing","media services","content creation","broadcasting"]
]

def get_industry(overview):
    if pd.isna(overview) or not overview.strip():
        return 'Other'
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
          {
            "role": "user",
            "content": 
            f"You are a cheerful assitant that will help assign correct industry mappings to a list of campanies in a csv file\n"
            f"Read the following company overview and assign the correct industry from the given list: {overview}\n\nIndustries: {industries}\n"
            f"It can be any item from the array. But must be the complete item at index\n"
            f"for a finance related company it should be: finance, banking, financial, investment, insurance, wealth management, asset management, financial planning, fintech, financial technology, Financial Services, venture, capital, venture capital, equity\n"
            f"if you think it is a tech related company, it should be: tech, it, technology, technology services, information technology, software development, IT consulting, IT services, cybersecurity, cloud computing, data analytics, AI, artificial intelligence, machine learning, network security, computer networks\n"
            f"Please dont assign like Industry: all the industry mappins, do as i just explained\n"
            f"And dont copy paste the array as is, it should joined as i explained to you above\n"
          }
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

# Read the CSV file
df = pd.read_csv('company_info.csv')

# Process each row and update the mapped_industry column only if company_overview exists
df['mapped_industry'] = df['company_overview'].apply(lambda x: get_industry(x) if pd.notna(x) and x.strip() else 'Other')

# Save the updated dataframe to a new CSV file
df.to_csv('company_info_new.csv', index=False)

print("Industries updated and saved to 'company_info_new.csv'.")