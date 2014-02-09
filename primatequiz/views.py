from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from primatequiz.models import *



# Create your views here.
def renderBase(request):
    return render_to_response("basic_bootstrap.html", context_instance=RequestContext(request))

def quiz(request):
    questions = question.objects.all()
    pastels = ["#F7977A","#F9AD81","#FDC68A","#FFF79A","#C4DF9B","#A2D39C","#82CA9D","#7BCDC8","#6ECFF6","#7EA7D8","#8493CA","#A187BE","#BC8DBF","#F49AC2","#F6989D"]
    return render_to_response("splashpage.html",
                                    {"questions":questions, "pastels":pastels},
                                    context_instance=RequestContext(request))

def results(request, slug=None):
    if not slug:
        return HttpResponseRedirect("/")
    else:
        rez = get_object_or_404(species, slug = slug)

    if rez:
        return render_to_response("results.html",
                                    {"species":rez},
                                    context_instance=RequestContext(request))

