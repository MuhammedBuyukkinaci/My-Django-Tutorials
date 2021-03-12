from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def homepage(request):
    # HTML can be below as a parameter to HttpResponse
    return HttpResponse("This is a <strong> NEW </strong> tutorial")


