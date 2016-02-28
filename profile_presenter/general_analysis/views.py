from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext

from profile_presenter.git_api_interactions import *

def index(request):

	username = ""

	if request.method == 'POST':
		username = str(request.POST.get('usename', ''))

	print username

	return render(request, 'my_profile/my_profile.html')

