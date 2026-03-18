# AI Image Analysis App (Azure Computer Vision)

## 🚀 Overview
This project is an AI-powered image analysis application built using Microsoft Azure Computer Vision API. It analyzes an image from a URL and generates a human-readable description of the image.

## 🧠 What It Does
- Sends an image URL to Azure AI Vision API
- Processes the image using AI
- Returns a descriptive caption of the image

Example Output:
AI Result:
a dog standing on a brick surface

## 🛠️ Technologies Used
- Python
- Microsoft Azure Computer Vision API
- REST API
- Requests Library

## 🔐 Security
This project uses environment variables to securely manage API credentials.

```python
AZURE_KEY = os.getenv("AZURE_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
