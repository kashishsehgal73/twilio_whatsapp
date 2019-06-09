from pymongo import MongoClient
client = MongoClient("mongodb+srv://kashish:chayansehgal3@cluster0-763oj.mongodb.net/test?retryWrites=true&w=majority")
database = client.get_database('cricket_db')
records = database.messages



def update_records(session_id, top, loc, cit):
	if top:
		records.update_one({'from': session_id}, {'$set': {'news_type': top }}, upsert=True)
	if loc:
		records.update_one({'from': session_id}, {'$set': {'geo-country': loc }}, upsert=True)
	if cit:
		records.update_one({'from': session_id}, {'$set': {'geo-city': cit }}, upsert=True)
	user_details = records.find({'from': session_id})[0]
	return user_details['news_type'], user_details['geo-country'], user_details['geo-city']
