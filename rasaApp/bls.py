import flask
from flask import Flask, request, jsonify
import json
import requests
import rasaApp


@rasaApp.app.route('/', methods=['GET', 'POST'])
def show_index():
    """Show the index page."""
    
    if flask.request.method == 'POST':
        # user's chat
        incoming = request.get_json()
        chat = incoming["text"]

        # send their message to rasa
        obj = {"sender": "Rasa", "message": chat}
        obj = json.dumps(obj)
        chat = requests.post("http://localhost:5005/webhooks/rest/webhook", data=obj)
        
        # decode the response
        rasa_resp = chat.json()
        rasa_resp = rasa_resp[0]["text"] 

        print(rasa_resp)
        return rasa_resp, 200

    return flask.render_template("index.html")