from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to central jail </h1> ")
def about(request):
    return HttpResponse("<h2>This is Jagal Ser</h2>")