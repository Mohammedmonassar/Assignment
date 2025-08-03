from django.shortcuts import render
from django.http import HttpResponse

def view_pages2(request):
    return HttpResponse("This is app2")

# Create your views here.
