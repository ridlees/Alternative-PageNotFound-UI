#!/bin/python3

import requests as r
from bs4 import BeautifulSoup as bs

from flask import Flask, render_template,request, send_from_directory
import os
from os.path import join, dirname

app = Flask(__name__, template_folder='./conf/templates')

def get(url):
    page = r.get(url)
    return page

def soup(page):
    return bs(page.content, 'html.parser')
    

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sender", methods=['POST', "GET"])
def send():
    if request.method == "GET":
        return "USE POST", 403
    
    if request.method == 'POST':
        url = request.form.get("url")
        PageNotFound = soup(get(url))
        spans = PageNotFound.find_all("span")[0:2]
        paragraphs = PageNotFound.find_all("p")

        text = str(spans) + "\n\n" + str(paragraphs)
            
        
        return f"<p class=center> {text} </p>", 201
    
app.run(host="0.0.0.0",port=80)
