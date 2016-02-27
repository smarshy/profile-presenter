from django.shortcuts import render_to_response
from django.template import RequestContext

from profile_presenter.git_api_interactions import *

def index(request):
    return render_to_response('my_profile/my_profile.html', context_instance=RequestContext(request))

