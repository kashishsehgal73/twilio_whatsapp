from pymongo import MongoClient
client = MongoClient("mongodb+srv://kashish:chayansehgal3@cluster0-763oj.mongodb.net/test?retryWrites=true&w=majority")
database = client.get_database('cricket_db')
db = database.messages
def data_dict(**data):
	return data

def upload(sess_id, message_received, message_sent):
	db.insert_one(data_dict(session_id = sess_id, message_received = message_received, message_sent = message_sent))
	return
