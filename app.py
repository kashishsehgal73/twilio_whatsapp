from flask import Flask, request
import os
from twilio.twiml.messaging_response import MessagingResponse
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "ks73wbot-kwqfwu-8d044c465d30.json"

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "ks73wbot-kwqfwu"

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello, World!"

@app.route("/sms", methods=['POST','GET'])
def sms_reply():
	if request.method == 'GET':

		resp = detect_intent_from_text('show me sports news',1234)
		resp = resp.fulfillment_text

		response = MessagingResponse()
		response.message(resp)

		return str(resp)

	else: 
		msg = request.form.get('Body')
		#resp = detect_intent_from_text('show me sports news',1234)
		#resp = resp.fulfillment_text

		response = MessagingResponse()
		#response.message(resp)
		
		response.message("You said: {}".format(msg))
		return str(response)




def detect_intent_from_text(text, session_id, language_code='en'):
	session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
	text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
	query_input = dialogflow.types.QueryInput(text=text_input)
	response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
	return response.query_result

if __name__ == "__main__":
	app.run(use_reloader=True)
