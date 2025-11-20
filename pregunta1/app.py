from flask import Flask, jsonify
import requests

app = Flask(__name__)

API = "https://api.exchangerate.host/latest?base=USD"

@app.route("/")
def get_rates():
    r = requests.get(API).json()
    rates = {
        "dolar": 1,
        "euro": r["rates"]["EUR"],
        "sol": r["rates"]["PEN"]
    }
    return jsonify(rates)
