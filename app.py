from flask import Flask, request
import os
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "ks73wbot-kwqfwu"

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():

	print(request.form)
	msg = request.form.get('Body')
	sender = request.form.get('From')
	resp = fetch_reply(msg,sender)
	response = MessagingResponse()
	response.message(resp)

	#response.message("You said: {}".format(msg))
	return str(response)



if __name__ == "__main__":
	app.run(use_reloader=True)
