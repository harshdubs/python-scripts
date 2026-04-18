import requests
import os

api_key = os.environ.get("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"
chat = []


Ole = {
    "Authorization":  f"Bearer {api_key}",
    "Content-Type": "application/json"
}
chat = {
    "model": "llama-3.1-8b-instant",
    "messages": [
        {"role": "system", "content": "You are a helpful data analyst assistant who gives concise answers."}
    ]
}

while True:
    
    user_input = input("\nYou:")
    if user_input == "exit" or user_input == "quit":
        exit()
    
    chat["messages"].append({"role": "user", "content": user_input })

    post = requests.post(url, headers=Ole, json=chat)
    print(f"Bot: {post.json()["choices"][0]["message"]["content"]}")
    chat["messages"].append({"role": "assistant", "content":post.json()["choices"][0]["message"]["content"]})
    
    