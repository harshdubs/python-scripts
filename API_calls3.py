import requests
import os
api_key = os.environ.get("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"

payload = {
    "model": "llama-3.1-8b-instant",
    "messages": [
        {"role": "system", "content": "You are a helpful data analyst assistant who gives concise answers."},
        {"role": "user", "content": "Hi gpt, which model am i working on?"}
    ]
}

Ole = {
    "Authorization":  f"Bearer {api_key}",
    "Content-Type": "application/json"
}

post = requests.post(url, headers=Ole, json=payload)

print(post.status_code)

print(post.json()["choices"][0]["message"]["content"])