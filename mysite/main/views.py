from django.shortcuts import render

from django.http import HttpResponse

from .models import Tutorial

# Create your views here.

def homepage(request):
    # HTML can be below as a parameter to HttpResponse
    #return HttpResponse("This is a <strong> NEW </strong> tutorial")
    return render( request = request, 
    template_name = "main/home.html", 
    context = {"tutorials": Tutorial.objects.all} )

