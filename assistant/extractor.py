
from openai import OpenAI

client = OpenAI()
from data.prompt_templates import CATEGORY_EXTRACTION_PROMPT, DELIMITER
import ast

def extract_categories_and_products(user_query):
    prompt = CATEGORY_EXTRACTION_PROMPT + f"\n{DELIMITER}{user_query}{DELIMITER}"

    response = client.chat.completions.create(model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0)

    try:
        return ast.literal_eval(response.choices[0].message.content)
    except Exception as e:
        print("Extraction error:", e)
        return []
