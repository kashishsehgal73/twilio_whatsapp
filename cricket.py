
from cric_api import kashish_assistant
c = kashish_assistant()


def get_score(parameters):
	matches = c.matches()
	country = parameters.get('geo-country')
	message = []
	for match in matches:
		if ((country in match["team1"]["name"] ) or (country in match["team2"]["name"] )):
			mid = match["id"]
			if match['mchstate'] != 'mom' or match['mchstate'] != 'completed':
				return (match['status'])
			message =  match_details(mid)
			print(message)
			return message
	return "Sorry"

def list_matches(parameters):
	matches = c.matches()
	print("##########################################", type(matches))
	message = []
	for match in matches:
		names = str(match["team1"]["name"] +" " + match["team2"]["name"]+ "\n\n" )
		details = "\n".join([match["srs"], names, match["mnum"], match["status"]])
		message.append(details)
		print(message)
	return "\n".join(message)


def match_details(mid):
	lscore = c.scorecard(mid)
	t1 = lscore["scorecard"][0]
	team1 = t1["batteam"]
	team1_score = t1["batcard"]

	scorecard = []
	scorecard.append("*{}*".format(team1))
	for i in team1_score:
		card = i["name"] + " : "+ i["runs"]
		scorecard.append(card)

	scorecard.append(str("*Overs*: " + str(t1["overs"]) + " \n*Score*: " + str(t1["runs"]) +"/" + str(t1["wickets"] + "\n\n")))



	t2 = lscore["scorecard"][1]
	team2 = t2["batteam"]
	scorecard.append("*{}*".format(team2))
	team2_score = t2["batcard"]
	for i in team2_score:
		card = i["name"] + " : "+ i["runs"]
		scorecard.append(card)

	scorecard.append(str("*Overs*: " + str(t2["overs"]) + " \nScore: " + str(t2["runs"]) +"/" + str(t2["wickets"])))
	return("\n".join(scorecard))
