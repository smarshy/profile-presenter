import requests
from collections import defaultdict

def get_response(url):

	r = requests.get(url)
	response = r.json()
	return response

def get_count(url):

	r = requests.get(url)
	response = r.json()
	return response['total_count']

def get_items(url):

	r = requests.get(url)
	response = r.json()
	return response['items']

def get_contributions_analysis(username):

	statistics = {}
	url = "https://api.github.com/search/issues?q=author:" + str(username) + "+type:"

	url1 = url + "issue" + "&?access_token=22f95e569456a47a3b18088588d2d70f63a1fec4"
	url2 = url + "pr" + "&?access_token=22f95e569456a47a3b18088588d2d70f63a1fec4"
	url3 = url + "pr+is:open" + "&?access_token=22f95e569456a47a3b18088588d2d70f63a1fec4"
	url4 = url + "pr+is:closed+is:unmerged" + "&?access_token=22f95e569456a47a3b18088588d2d70f63a1fec4"
	url5 = url + "pr+is:closed+is:merged" + "&?access_token=22f95e569456a47a3b18088588d2d70f63a1fec4"

	try:
		statistics['issues'] = get_count(url1)
		statistics['prs'] = get_count(url2)
		if statistics['issues'] or statistics['prs']:
			statistics['open_prs'] = get_count(url3)
			statistics['unmerged_prs'] = get_count(url4)
			statistics['merged_prs'] = get_count(url5)	
		else:
			return {}
	except:
		print "Check if username is valid/internet connection"
		return False

	return statistics

def get_language_analysis(username):

	languages = []
	my_lang = {}

	url = "https://api.github.com/search/repositories?q=fork:false+user:" + username + "&?access_token=22f95e569456a47a3b18088588d2d70f63a1fec4"
	try:
		repos = get_items(url)
	except:
		print "Check if username is valid/internet connection"
		return False

	for repo in repos:
		if repo['language']:
			languages.append(repo['language'])

	analysed = defaultdict(int)

	for language in languages:
		analysed[language] += 1

	for key,value in analysed.items():
		my_lang[str(key)] = value

	return my_lang

def get_commit_analysis(username):

	repositories = []

	days_count = {}
	days_count['sunday'] = 0
	days_count['monday'] = 0
	days_count['tuesday'] = 0
	days_count['wednesday'] = 0
	days_count['thursday'] = 0
	days_count['friday'] = 0
	days_count['saturday'] = 0


	url = "https://api.github.com/users/" + username  + "/repos" + "?access_token=22f95e569456a47a3b18088588d2d70f63a1fec4"

	try:
		repos = get_response(url)
	except:
		print "Check if username is valid/internet connection"
		return False

	for repo in repos:
		if not repo['fork'] and not repo['private']:
			repositories.append(str(repo['full_name']))

	for repo in repositories:
		url_for_repo = "https://api.github.com/repos/" + str(repo) + "/stats/commit_activity" + "?access_token=22f95e569456a47a3b18088588d2d70f63a1fec4"
		try:
			data = get_response(url_for_repo)
			if data:
				recent = [data[-1]['days'], data[-2]['days'], data[-3]['days'], data[-4]['days']]

				for week in recent:
					days_count['sunday'] += week[0]
					days_count['monday'] += week[1]
					days_count['tuesday'] += week[2]
					days_count['wednesday'] += week[3]
					days_count['thursday'] += week[4]
					days_count['friday'] += week[5]
					days_count['saturday'] += week[6]				

			else:
				print "Slow Internet Connection"
		except:
			print "Error in internet connection"
			return False

	return days_count

def get_contributions_list(username):

	url = "https://api.github.com/search/issues?q=author:" + username + "+type:"

	pr_list = []
	issue_list = []

	url1 = url + "issue" + "&?access_token=22f95e569456a47a3b18088588d2d70f63a1fec4"
	url2 = url + "pr" + "&?access_token=22f95e569456a47a3b18088588d2d70f63a1fec4"

	try:
		issues = get_items(url1)
		prs = get_items(url2)
	except:
		print "Check if username is valid/internet connection"
		return False

	for pr in prs:
		pr_list.append(str(pr['html_url']))

	for issue in issues:
		issue_list.append(str(issue['html_url'])) 

	return {'prs':pr_list, 'issues':issue_list}