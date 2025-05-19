
import os
from dotenv import load_dotenv
import openai
from assistant.pipeline import run_assistant_pipeline_with_memory
import panel as pn

load_dotenv()

pn.extension(design="material")
chat_history = pn.Column()
user_input = pn.widgets.TextInput(placeholder="Ask a tech product question...", width=600)
submit_button = pn.widgets.Button(name="Send", button_type="primary", width=100)

def submit_handler(event):
    query = user_input.value.strip()
    if query:
        chat_history.append(pn.pane.Markdown(f"**You:** {query}"))
        reply = run_assistant_pipeline_with_memory(query)
        chat_history.append(pn.pane.Markdown(f"**Assistant:** {reply}"))
        user_input.value = ""

submit_button.on_click(submit_handler)
chat_interface = pn.Column(
    pn.pane.Markdown("### 🛒 Tech Shop Assistant Chatbot"),
    chat_history,
    pn.Row(user_input, submit_button),
    sizing_mode="stretch_width"
)

chat_interface.servable()
