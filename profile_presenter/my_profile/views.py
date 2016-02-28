from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext

from profile_presenter.git_api_interactions import *

def index(request):
	username = "smarshy"
	languages = get_language_analysis(username)
	stats = get_contributions_analysis(username)
	commit_act = get_commit_analysis(username)
	print stats
	print languages
	print commit_act
	return render(request, 'my_profile/my_profile.html', {'stats': stats, 'user': username, 'languages': languages, 'commit': commit_act})

