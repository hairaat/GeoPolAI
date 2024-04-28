import os
import json
import requests

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
  # Preprocess text
  text = text.strip()

  # Query LLM
  response = query_llm(text)

  # Print response
  print(response)

# Main loop
while True:
  # Get user input
  text = input("Ask me anything about geopolitics or international relations: ")

  # Handle input
  handle_input(text)
