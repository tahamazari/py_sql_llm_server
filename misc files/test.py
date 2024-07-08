array = ["It", "Hospitality", "software", "IT Services and IT Consulting", "Financial Services", "ocean"]

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
}

# Function to find the best matching industry and return its values
def find_best_match(item, industry_mapping):
    best_match = None
    max_matched_words = 0
    
    for industry, mappings in industry_mapping.items():
        matched_words = sum(1 for word in item.lower().split() if any(word in mapping.lower().split() for mapping in mappings))
        
        if matched_words > max_matched_words:
            max_matched_words = matched_words
            best_match = mappings
    
    return best_match if best_match else [f"{item}"]

# Replace array values with corresponding mappings' values
new_array = []
for item in array:
    matched_values = find_best_match(item, industry_mapping)
    new_array.append(", ".join(matched_values))

print(new_array)
