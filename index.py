from flask import Flask, request, jsonify
from rasa.core.agent import Agent

app = Flask(__name__)

# Load the Rasa chatbot model
bot_agent = Agent.load("models/20231026-172237-crunchy-chickadee.tar.gz")

@app.route("/webhook", methods=["POST"])
def webhook():
    user_message = request.json.get("user_message")

    # Send the user's message to the Rasa model
    response = bot_agent.handle_text(user_message)
    print(response)
    # Extract the bot's response
    bot_response = response[0]["text"]

    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)