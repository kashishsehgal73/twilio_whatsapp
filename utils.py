from cricket import get_score,list_matches
from functions import get_news,get_weather,get_fact
import dialogflow_v2 as dialogflow
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "client-secret.json"
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "ks73wbot-kwqfwu"


#Detecting intent from the text sent by the user
def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result


#Detects the intent and call the respective funtions for each different intent
def fetch_reply(msg, session_id):
	response = detect_intent_from_text(msg, session_id)
	print(dict(response.parameters))
	try:
		if response.intent.display_name == 'get_news':
			value =  get_news(dict(response.parameters),session_id)
		elif response.intent.display_name == 'get_weather':
			value =  get_weather(dict(response.parameters),session_id)
		elif response.intent.display_name == 'cricket_score':
			value =  get_score(dict(response.parameters))
		elif response.intent.display_name == 'match_list':
			value = list_matches(dict(response.parameters))
		elif response.intent.display_name == 'number_fact':
			value = get_fact(dict(response.parameters))
		else:
			value = response.fulfillment_text
		return value
	except Exception as e:
		print(e)
		return "Oops! Looks like my cricket buddy is facing some problems and is not able to tell me the info right now. Try my other functions till then"
