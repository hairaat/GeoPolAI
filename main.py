import os
import json
import requests
import nltk
from nltk.tokenize import word_tokenize

# Load LLM API key
api_key = os.environ.get("LLM_API_KEY")

# Define function to query LLM
def query_llm(prompt):
    url = "https://api.llm.ai/v1/generate"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {"prompt": prompt, "max_tokens": 1000}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["text"]

# Define function to handle user input
def handle_input(text):
    # Tokenize and lowercase the input text
    tokens = word_tokenize(text.lower())

    # Query LLM with preprocessed text
    response = query_llm(' '.join(tokens))

    # Print response
    print(response)

# Main block
if __name__ == "__main__":
    # Get LLM API key
    api_key = "YOUR_LLM_API_KEY"

    # Prompt user for input
    while True:
        # Get user input
        text = input("Ask me anything about geopolitics or international relations: ")

        # Handle input
        handle_input(text)
