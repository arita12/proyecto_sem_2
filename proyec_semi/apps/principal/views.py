from django.shortcuts import render, render_to_response
from django.template import RequestContext


def inicio_view(request):
    return render_to_response("principal/inicio.html", {}, context_instance=RequestContext(request))