import pandas as pd
from fuzzywuzzy import process

# Define your industry mappings (shortened for brevity)
industry_mapping = {
    "Information Technology & Services": [
        "tech", "it", "technology", "technology services", "information technology", 
        "software development", "IT consulting", "IT services", "cybersecurity", 
        "cloud computing", "data analytics", "AI", "artificial intelligence", 
        "machine learning", "network security", "computer networks"
    ],
    "Financial Services": [
        "finance", "banking", "financial", "investment", "insurance", 
        "wealth management", "asset management", "financial planning", 
        "fintech", "financial technology", "Financial Services", "venture", "capital", "venture capital", "equity"
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
        "retail", "shopping", "online shopping", "ecommerce", "store", 
        "online store", "consumer goods", "retail sales", "cosmetics"
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
    "Nonprofit Non-profit Organization": [
        "nonprofit", "non-profit","charity", "ngo", "non-governmental organization", 
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
    "Pharmaceutical & Pharmaceutical Manufacturing": [
        "pharmaceuticals", "drug", "medicine", "biotech", "biotechnology", "pharmaceutical" 
        "pharmaceutical services", "drug development", "clinical trials", 
        "healthcare products", "Pharmaceutical Manufacturing", "Pharmaceuticals Manufacturing"
    ],
    "Aerospace Airlines & Avionics": [
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

# Function to find the best matching industry and return its values as a formatted string
def find_best_match(item, industry_mapping):
    if pd.isna(item):  # Handle NaN values
        return "Other"
    
    best_match = None
    max_matched_words = 0
    best_mappings = []
    
    # Iterate over each industry and its mappings
    for industry, mappings in industry_mapping.items():
        # Count how many words in item match any words in mappings
        matched_words = sum(1 for word in str(item).lower().split() if any(word in mapping.lower().split() for mapping in mappings))
        
        # Keep track of the industry with the maximum matched words
        if matched_words > max_matched_words:
            max_matched_words = matched_words
            best_match = industry
            best_mappings = mappings
    
    # Format the best mappings as a string without brackets, commas, and spaces
    return ", ".join(best_mappings) if best_match else "Other"  # Return the mappings of the best matching industry or "Other" if no match

# Load the CSV file
file_path = './data-1719989221413.csv'
df = pd.read_csv(file_path)

# Apply the mapping function to each row in the 'company_industry' column
df['mapped_industry'] = df['company_industry'].apply(lambda x: find_best_match(x, industry_mapping))

# Save the updated dataframe to a new CSV file
output_file_path = 'updated_data_with_mappings.csv'
df.to_csv(output_file_path, index=False)

print(f"Updated data saved to {output_file_path}")