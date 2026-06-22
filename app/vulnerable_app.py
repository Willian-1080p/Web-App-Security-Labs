from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Web Security Lab"

@app.route("/search")
def search():
    query = request.args.get("q")
    return f"Results for: {query}"

app.run(debug=True)
