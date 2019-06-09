from flask import Flask, request
import os
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse
import requests
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
	msg = request.form.get('Body')
	sender = request.form.get('From')
	# The reply object
	resp = MessagingResponse()

	#Calling function to generate reply
	rec_reply = fetch_reply(msg,sender)

	# If a simple string is returned print that string
	if type(rec_reply) == str:
		message = Message()
		message.body(rec_reply)
		resp.append(message)
		return str(resp)

	# If 2 objects (string and url are returned append the media to message and send)
	for row in rec_reply:
		message = Message()
		link = requests.get('http://tinyurl.com/api-create.php?url={}'.format(row['link'])).content.decode('utf-8')
		message.body("{}\n{}".format(row['title'],link))
		if row['media'] :
			message.media(row['media'])
		resp.append(message)
	return str(resp)

if __name__ == "__main__":
	app.run(use_reloader=True)
