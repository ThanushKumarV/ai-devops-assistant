import requests
import os

API_KEY = os.getenv("OPENROUTER_API_KEY")

def analyze_logs(logs):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-3-8b-instruct",  # free model
            "messages": [
                {"role": "system", "content": "You are a DevOps expert."},
                {"role": "user", "content": f"Analyze this CI/CD error log and give root cause + fix:\n{logs}"}
            ]
        }
    )

    return response.json()["choices"][0]["message"]["content"]


if __name__ == "__main__":
    with open("error.log", "r") as f:
        logs = f.read()

    result = analyze_logs(logs)
    print("\n🔍 AI Analysis:\n")
    print(result)

    API_KEY = os.getenv("OPENROUTER_API_KEY")
