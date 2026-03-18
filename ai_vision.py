import requests
import os

AZURE_KEY = os.getenv("AZURE_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")

analyze_url = AZURE_ENDPOINT + "vision/v3.2/analyze"

headers = {
    "Ocp-Apim-Subscription-Key": AZURE_KEY,
    "Content-Type": "application/json"
}

params = {
    "visualFeatures": "Description"
}

data = {
    "url": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Pug_600.jpg"
}

response = requests.post(analyze_url, headers=headers, params=params, json=data)
result = response.json()

print("AI Result:")
print(result["description"]["captions"][0]["text"])