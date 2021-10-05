from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def print_page_name(request):
    return HttpResponse("This is the page for TMT-B")
