import os
from gnewsclient import gnewsclient
from cricket import get_score,list_matches
from database import upload

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client-secret.json"

import dialogflow_v2 as dialogflow
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "ks73wbot-kwqfwu"
client = gnewsclient.NewsClient()

def get_news(parameters):
	client.topic = parameters.get('news_type')
	client.language = parameters.get('language')
	client.location = parameters.get('geo-country')
	return str(client.get_news())

def detect_intent_from_text(text, session_id, language_code='en'):
	session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
	text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
	query_input = dialogflow.types.QueryInput(text=text_input)
	response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
	return response.query_result


def fetch_reply(msg, session_id):
	try:
		response = detect_intent_from_text(msg, session_id)
		if response.intent.display_name == 'get_news':
			vaue =  get_news(dict(response.parameters))
		elif response.intent.display_name == 'cricket_score':
			value =  get_score(dict(response.parameters))
		elif response.intent.display_name == 'match_list':
			value =  list_matches(dict(response.parameters))
		else:
			value =  response.fulfillment_text
	upload(session_id, msg, value)
	return value
