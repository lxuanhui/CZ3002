from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'Home.html')

def TMT_A(request):
    return render(request,"TMT_A.html")

def TMT_B(request):
    return render(request,'TMT_B.html')