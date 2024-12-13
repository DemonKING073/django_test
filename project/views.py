from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def projects(request):
    return HttpResponse('This is our projects page!')

def project (request, pid):
    return HttpResponse('This is project '+ str(pid) + ' page!')
