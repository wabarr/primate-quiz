from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def renderBase(request):
    return render_to_response("basic_bootstrap.html", context_instance=RequestContext(request))