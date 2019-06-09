from pymongo import MongoClient
client = MongoClient("mongodb+srv://kashish:chayansehgal3@cluster0-763oj.mongodb.net/test?retryWrites=true&w=majority")
database = client.get_database('cricket_db')
db = database.messages



def update_records(session_id, top, loc, cit):
	if top:
		db.people.update_one({'from': session_id}, {'$set': {'news_type': top }}, upsert=True)
	if loc:
		db.people.update_one({'from': session_id}, {'$set': {'geo-country': loc }}, upsert=True)
	if cit:
		db.people.update_one({'from': session_id}, {'$set': {'geo-city': cit }}, upsert=True)
	a = records.find({'from': session_id})[0]
	return a['news_type'], a['geo-country'], a['geo-city']

def data_dict(**data):
	return data

def upload(sess_id, message_received, message_sent):
	db.insert_one(data_dict(session_id = sess_id, message_received = message_received, message_sent = message_sent))
	return
