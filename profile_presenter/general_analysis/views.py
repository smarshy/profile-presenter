from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext

from profile_presenter.git_api_interactions import *

def index(request):

	username = ""

	if request.method == 'POST':
		username = str(request.POST.get('usename', ''))
	print username

	if not username:
		return render_to_response('general_analysis/missing_entry.html', context_instance=RequestContext(request))

	languages = get_language_analysis(username)
	stats = get_contributions_analysis(username)
	commit_act = get_commit_analysis(username)
	print stats
	print languages
	print commit_act

	if languages and stats and commit_act:
		return render(request, 'general_analysis/display_analysis.html', {'stats': stats, 'user': username, 'languages': languages, 'commit': commit_act})
	else:
		return render_to_response('general_analysis/error_page.html', context_instance=RequestContext(request))

