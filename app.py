import requests
import logging
from flask import Flask, request, make_response

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

SITE_URL = "https://zuyd.nl"
CSS = "<style> body {transform: scale(2.5, 0.9);} img {filter: grayscale(50%) contrast(2000%); transform: scaleX(1.5)}</style>"
JS = "<script>document.querySelectorAll('span, p, h1, h2, h3, h4, a').forEach(element => {element.innerText = element.innerText.replaceAll(/b/gi, '🅱️')})</script>"

@app.route('/')
def handle():
    app.logger.info(f"Serving request")
    r = requests.get(SITE_URL)
    boi = CSS + r.text + JS
    return boi, r.status_code

@app.errorhandler(404)
def proxy(e):
    r = requests.get(SITE_URL + request.path)

    if r.headers.get("Content-Type").split(";")[0] == "text/html":
        content = CSS + r.text + JS
    else:
        content = r.content

    s = make_response(content, r.status_code)
    s.headers["Content-Type"] = r.headers.get("Content-Type", "text/html")

    return s

