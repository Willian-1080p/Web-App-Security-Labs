from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    return "Web Security Lab"

@app.route("/search")
def search():
    query = escape(request.args.get("q"))
    return f"Results for: {query}"

app.run(debug=True)
