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
	# Create reply
	resp = MessagingResponse()
	recieved_obj = fetch_reply(msg,sender)

	# If the recieved object is from get_weather()
	if isinstance(recieved_obj[0], str):
		message = Message()
		message.body(recieved_obj[0])
		message.media(recieved_obj[1])
		resp.append(message)
		return str(resp)

	# If the recieved object is from get_news()
	for row in recieved_obj:
		message = Message()
		link = requests.get('http://tinyurl.com/api-create.php?url={}'.format(row['link'])).content.decode('utf-8')
		message.body("{}\n{}".format(row['title'],link))
		if row['media'] :
			message.media(row['media'])
		resp.append(message)
	return str(resp)

if __name__ == "__main__":
	app.run(use_reloader=True)
