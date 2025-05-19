
from assistant.extractor import extract_categories_and_products
from assistant.responder import generate_reply
from data.product_data import get_products_by_category, get_products_by_name_fuzzy

def fetch_matching_products(extracted_info):
    matched = []
    for item in extracted_info:
        if 'category' in item:
            matched.extend(get_products_by_category(item['category']))
        elif 'products' in item:
            matched.extend(get_products_by_name_fuzzy(item['products']))
    return matched

def run_assistant_pipeline(user_query):
    extracted_info = extract_categories_and_products(user_query)
    matched_products = fetch_matching_products(extracted_info)
    return generate_reply(user_query, extracted_info, matched_products)

# ✅ Enhanced version with simple memory
conversation_context = {
    "last_query": None,
    "last_info": [],
    "last_products": []
}

def run_assistant_pipeline_with_memory(user_query):
    extracted_info = extract_categories_and_products(user_query)

    if not extracted_info and conversation_context["last_products"]:
        # fallback to last known context
        extracted_info = conversation_context["last_info"]
        matched_products = conversation_context["last_products"]
    else:
        matched_products = fetch_matching_products(extracted_info)
        # update memory
        conversation_context["last_query"] = user_query
        conversation_context["last_info"] = extracted_info
        conversation_context["last_products"] = matched_products

    return generate_reply(user_query, extracted_info, matched_products)
