from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
	return render_to_response('general_analysis/display_analysis.html', context_instance=RequestContext(request))

