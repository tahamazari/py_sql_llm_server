import pandas as pd
from fuzzywuzzy import process

# Load the CSV file
file_path = './data-1719989221413.csv'
df = pd.read_csv(file_path)

# Define the extended industry mapping
industry_mapping = {
    "Information Technology & Services": [
        "tech", "it", "technology", "technology services", "information technology", 
        "software development", "IT consulting", "IT services", "cybersecurity", 
        "cloud computing", "data analytics", "AI", "artificial intelligence", 
        "machine learning"
    ],
    "Financial Services": [
        "finance", "banking", "financial", "investment", "insurance", 
        "wealth management", "asset management", "financial planning", 
        "fintech", "financial technology", "Financial Services"
    ],
    "Maritime Transportation": [
        "maritime", "transportation", "shipping", "logistics", 
        "freight", "ocean transport", "sea transport"
    ],
    "Staffing and Recruiting": [
        "staffing", "recruiting", "recruitment", "hiring", "talent acquisition", 
        "HR services", "human resources", "employment services"
    ],
    "Healthcare": [
        "health", "medical", "hospital", "clinic", "healthcare", 
        "patient care", "medical services", "pharmaceutical", 
        "biomedical", "biotech", "biotechnology", "life sciences"
    ],
    "Manufacturing": [
        "manufacturing", "production", "factory", "industrial", 
        "manufacturing plant", "assembly line", "mass production"
    ],
    "Retail": [
        "retail", "shopping", "ecommerce", "store", "online store", 
        "brick and mortar", "consumer goods", "retail sales"
    ],
    "Education": [
        "education", "school", "university", "college", "learning", 
        "online education", "e-learning", "educational services"
    ],
    "Construction": [
        "construction", "building", "contractor", "infrastructure", 
        "civil engineering", "construction services", "real estate development"
    ],
    "Consulting": [
        "consulting", "advisory", "consultant", "business consulting", 
        "management consulting", "strategy consulting", "professional services"
    ],
    "Real Estate": [
        "real estate", "property", "housing", "realty", "real estate services", 
        "property management", "real estate investment", "commercial real estate"
    ],
    "Telecommunications": [
        "telecommunications", "telecom", "communication", "network", 
        "wireless", "broadband", "internet services", "mobile services"
    ],
    "Energy": [
        "energy", "oil", "gas", "renewable", "power", "electricity", 
        "solar energy", "wind energy", "energy services", "energy production"
    ],
    "Automotive": [
        "automotive", "car", "vehicle", "auto", "automobile", 
        "car manufacturing", "vehicle production", "auto services"
    ],
    "Food and Beverage": [
        "food", "beverage", "restaurant", "cafe", "drink", "food services", 
        "hospitality", "catering", "food production", "beverage production"
    ],
    "Entertainment": [
        "entertainment", "media", "film", "music", "theater", 
        "broadcasting", "publishing", "content production", "multimedia"
    ],
    "Nonprofit": [
        "nonprofit", "charity", "ngo", "non-governmental organization", 
        "social services", "philanthropy", "volunteer services"
    ],
    "Government": [
        "government", "public sector", "municipal", "state", "federal", 
        "public administration", "government services", "public policy"
    ],
    "Agriculture": [
        "agriculture", "farming", "crop", "agro", "agribusiness", 
        "agricultural production", "livestock", "dairy farming"
    ],
    "Pharmaceuticals": [
        "pharmaceuticals", "drug", "medicine", "biotech", "biotechnology", 
        "pharmaceutical services", "drug development", "clinical trials", 
        "healthcare products"
    ],
    "Aerospace, Airlines & Avionics": [
        "aerospace", "aviation", "aircraft", "space", "defense", 
        "aerospace engineering", "aerospace manufacturing", "space exploration"
    ],
    "Hospitality": [
        "hospitality", "hotel", "resort", "travel", "tourism", 
        "lodging", "accommodation services", "hospitality management"
    ],
    "Transportation": [
        "transportation", "logistics", "freight", "delivery", "shipping", 
        "transport services", "cargo", "supply chain"
    ],
    "Legal Services": [
        "legal services", "law", "law firm", "attorney", "legal consulting", 
        "litigation", "legal advice", "corporate law"
    ],
    "Media and Communications": [
        "media", "communications", "public relations", "advertising", 
        "marketing", "media services", "content creation", "broadcasting"
    ]
}

def map_industry(industry, mapping):
    if isinstance(industry, str):
        for standard, variations in mapping.items():
          for variation in variations:
              print(industry.lower())
              if variation.lower() in industry.lower():
                  return ', '.join(variations)  # Return the variations as a comma-separated string
    return "Other"  # Use "Other" for unmatched industries

# Apply the mapping to the dataframe
df['mapping'] = df['company_industry'].apply(lambda x: map_industry(x, industry_mapping))

# # Save the updated dataframe to a new CSV file
# output_file_path = 'updated_data_with_mappings.csv'
# df.to_csv(output_file_path, index=False)
