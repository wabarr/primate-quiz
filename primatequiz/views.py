from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from primatequiz.models import *
from questions.models import question



# Create your views here.
def renderBase(request):
    return render_to_response("basic_bootstrap.html", context_instance=RequestContext(request))

def quiz(request):
    questions = question.objects.order_by('?')
    if len(questions) < 5:
        questions = questions
    else:
        questions = questions[0:4]
    result = species.objects.order_by('?')[0]
    return render_to_response("splashpage.html",
                                    {"questions":questions,"result":result},
                                    context_instance=RequestContext(request))

def results(request, slug=None):
    if not slug:
        rez = species.objects.order_by('?')[0]
    else:
        rez = get_object_or_404(species, slug = slug)

    if rez:
        return render_to_response("results.html",
                                    {"species":rez},
                                    context_instance=RequestContext(request))

