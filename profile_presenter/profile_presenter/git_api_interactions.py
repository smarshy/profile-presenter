import requests
from collections import defaultdict

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

	url1 = url + "issue"
	url2 = url + "pr"
	url3 = url + "pr+is:open"
	url4 = url + "pr+is:closed+is:unmerged"
	url5 = url + "pr+is:closed+is:merged"

	try:
		statistics['Total Issues'] = get_count(url1)
		statistics['Total PRs'] = get_count(url2)
		statistics['Open PRs'] = get_count(url3)
		statistics['Unmerged PRs'] = get_count(url4)
		statistics['Merged PRs'] = get_count(url5)	
	except:
		print "Check if username is valid/internet connection"
		return False

	return statistics

def get_language_analysis(username):

	languages = []
	url = "https://api.github.com/search/repositories?q=fork:false+user:" + username 
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

	return analysed.items()
