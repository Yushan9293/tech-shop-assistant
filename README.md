# Tech Shop Assistant

A GPT-4 powered product assistant chatbot for tech and electronics stores. Users can ask product-related questions in natural language, and the bot will extract product names or categories, match them against a product database, and respond with helpful suggestions.

---

## 🔧 Features

- **Fuzzy product name matching**  
  Handles user typos, partial matches, and informal phrasing. For example, typing "gamesphere" or "game spher" will successfully match the product "GameSphere Y" using case-insensitive fuzzy logic.

- **Memory-aware replies**  
  The assistant remembers previous product mentions from the conversation. If a user first asks "Show me TVs" and later says "Which is the cheapest?", the assistant will infer they are still referring to TVs.

- **Product/category extraction with GPT**  
  User questions are analyzed using GPT-4 to extract meaningful product names or category keywords (e.g. "cheap laptop" → category: "Computers and Laptops").

- **Custom prompt engineering**  
  GPT is guided by system prompts to behave like a friendly and knowledgeable in-store product advisor. It only recommends products from the structured database.

- **Panel UI**  
  Clean web-based chat interface using Panel, a Python GUI framework, with real-time input and dynamic response display.

---

## 🚀 Tech Stack

- OpenAI GPT-4 API
- Python 3
- Panel (for UI)
- Prompt Engineering
- Custom product database (structured dict format)

---

## 📸 Screenshots

_Add a screenshot here showing a chat example with fuzzy matching and follow-up queries._

---

## 📁 Project Structure

```
tech_shop_assistant/
├── assistant/
│   ├── extractor.py       # Extracts products/categories using GPT
│   ├── responder.py       # Formats prompts & parses responses
│   ├── pipeline.py        # Memory-aware logic pipeline
├── data/
│   ├── product_data.py    # Structured product info
│   ├── prompt_templates.py# System prompts
├── panel_app.py           # Web UI entry point
├── main.py                # Alt entry (optional)
```

---

## 🧪 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

3. Run the app:
```bash
panel serve panel_app.py --autoreload
```

The chatbot UI will open at `http://localhost:5006` in your browser.

---

## 📄 License

This project is for educational and demo purposes.
