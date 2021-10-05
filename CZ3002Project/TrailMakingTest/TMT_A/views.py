from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Takes a request and returns a response (request handler)

def print_page_name(request):
    return HttpResponse("This is the page for TMT-A")