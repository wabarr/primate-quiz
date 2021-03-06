from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from primatequiz.models import *
from questions.models import question


def quiz(request):
    if request.user.has_perm("primatequiz.delete_species"):
        useGoogleAnalytics =  False
    else:
        useGoogleAnalytics =  True
    questions = question.objects.order_by('?')
    if len(questions) < 5:
        questions = questions
    else:
        questions = questions[0:6]
    result = species.objects.order_by('?')[0]
    return render_to_response("splashpage.html",
                                    {"questions":questions,"result":result,"useGoogleAnalytics":useGoogleAnalytics},
                                    context_instance=RequestContext(request))

def results(request, slug=None):
    if request.user.has_perm("primatequiz.delete_species"):
        useGoogleAnalytics =  False
    else:
        useGoogleAnalytics =  True

    #If the get parameter indicates that this is from a facebook share,
    #then redirect to the main page for humans, but don't redirect facebook crawler, because we want to share results page
    if request.GET.get("fromSocialMedia","") == "T":
        if "facebookexternalhit" in request.META['HTTP_USER_AGENT']:
            pass
        else:
            return HttpResponseRedirect("/")

    if not slug:
        rez = species.objects.order_by('?')[0]
    else:
        rez = get_object_or_404(species, slug = slug)

    if rez:
        return render_to_response("results.html",
                                    {"species":rez,"useGoogleAnalytics":useGoogleAnalytics},
                                    context_instance=RequestContext(request))

