from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

def get_meme():
        url = "https://meme-api.com/gimme/Yappelkaas"
        response = json.loads(requests.request("GET", url).text)
        meme = response.url
        return meme


@app.route("/")
def index():
        meme = get_meme()
        return render_template("index.html", url=meme)


app.run(host="0.0.0.0", port=80)