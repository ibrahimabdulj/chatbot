from flask import Flask, render_template, request, jsonify
import chatbot_model  # your chatbot logic file

app = Flask(chatbot)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    # Call your chatbot function
    bot_reply = chatbot_model.get_response(user_message)

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
