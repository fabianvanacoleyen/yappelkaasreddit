from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

import requests

def get_meme():
    link = "https://meme-api.com/gimme/Yappelkaas"
    response = requests.get(link).json()  # Haalt de JSON data op van de API
    url = response.get('url')  # Retourneer de 'url' uit de JSON response
    title = response.get('title')
    print(title)
    return url, title



@app.route("/")
def index():
        url, title = get_meme()
        return render_template("index.html", url=url, title=title)


app.run(host="0.0.0.0", port=80)