from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from primatequiz.models import *


# Create your views here.
def renderBase(request):
    return render_to_response("basic_bootstrap.html", context_instance=RequestContext(request))

def quiz(request):
    return HttpResponse("this is the quiz")

def results(request, slug=None):
    if not slug:
        return HttpResponseRedirect("/primate_quiz/")
    else:
        rez = get_object_or_404(species, slug = slug)

    if rez:
        return render_to_response("results.html",
                                    {"species":rez},
                                    context_instance=RequestContext(request))

