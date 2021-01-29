from flask import Flask
from threading import Thread
import requests
import json
from datetime import date
from datetime import time
from datetime import datetime
from flask import Markup
from flask import Flask
from flask import render_template, flash, redirect
import os
from flask_mail import Mail, Message
from formatscript import formatjson

app = Flask('')

"""
5721600 - space gray m1 air 256gb
6418597 - silver
6418599 - gold
6200722 - space gray m1 air 512gb
6418598 - silver
6418600 - gold
5721600, 6418597, 6418599, 6200722, 6418598, 6418600
"""

def get_new():

	response = requests.get("https://api.bestbuy.com/beta/products/openBox(sku%20in(5721600,6418597,6418599,6200722,6418598,6418600))?apiKey=ZlmdCoCq2VFV0lRi9GVK5gM1")
	data = response.json()
	return data

data = get_new()

@app.route('/', methods=["GET", "POST"])
def home():

	"""
	print(data)
	new_data = {"items":[]}
	for i, x in enumerate(data["results"]):
		new_data["items"].append(x["names"])
		new_data["items"][i]["sku"] = (x["sku"])
		new_data["items"][i]["prices"] = (x["offers"])
	"""
	new_data = {"items":[]}

	for x in (data["results"]):
		new_data["items"].append(x)

	html_format = formatjson(new_data)

	return render_template('home.html', datastr=html_format)

def run():
  app.run(host='0.0.0.0',port=8080)

@app.route('/go')
def go():
    data = get_new()
    return redirect('/')

def keep_alive():  
    t = Thread(target=run)
    t.start()

keep_alive()
