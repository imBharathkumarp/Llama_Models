import requests

# This assumes you're trying to get a list of models from the Ollama API
response = requests.get("http://localhost:11434/api/tags")

# Print the response details BEFORE trying to parse JSON
print("Status code:", response.status_code)
print("Response text:", response.text)

try:
    data = response.json()
    print("Available models:", [m["name"] for m in data["models"]])
except Exception as e:
    print("Error parsing JSON:", e)
