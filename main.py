
import os
from dotenv import load_dotenv
import openai
from assistant.pipeline import run_assistant_pipeline

load_dotenv()

if __name__ == "__main__":
    query = input("Ask a tech product question: ")
    print(run_assistant_pipeline(query))
