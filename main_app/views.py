from django.shortcuts import render

# import HttpResponse to send text-based responses
from django.http import HttpResponse

# define the home view function
def home(request):
    #send a simple HTML response
    return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
    return HttpResponse('<h1>About the CatCollector<h1>')
