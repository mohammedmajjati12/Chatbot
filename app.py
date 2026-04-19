from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

my_api_key = os.getenv("MY_API_KEY")

app = Flask(__name__)
CORS(app)

with open("prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

client = OpenAI(
    api_key= my_api_key,
    base_url="https://api.mistral.ai/v1"
)

@app.route("/chat", methods=["GET","POST"])
def chat():
    user_message = request.json.get("pw")

    response = client.chat.completions.create(
        model="mistral-small",
        messages=[
            {"role": "system", "content": "You are an AI named Mohammed Majjati.Your role is: a strict teacher who explains concepts deeply.Rules:- Always respond in Arabic- Explain step by step- Give examples- Correct the user if they are wrong"},
            {"role": "user", "content": user_message}
        ]
    )

    return jsonify({
        "res": response.choices[0].message.content
    })

if __name__ == "__main__":
    app.run()
