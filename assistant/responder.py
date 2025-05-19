
from openai import OpenAI

client = OpenAI()
from data.prompt_templates import ASSISTANT_REPLY_PROMPT

def generate_reply(user_query, extracted_info, matched_products):
    system_prompt = ASSISTANT_REPLY_PROMPT.strip()
    message = {
        "role": "user",
        "content": f"""User question: {user_query}
Extracted info: {extracted_info}
Matching products: {matched_products}"""
    }

    response = client.chat.completions.create(model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        message
    ],
    temperature=0.7)

    return response.choices[0].message.content
