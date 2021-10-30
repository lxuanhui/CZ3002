from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = 'login')
def home(request):
    return render(request, 'home.html')

def TMTA(request):
    return render(request, 'TMTA.html')

def TMTB(request):
    return render(request,'TMTB.html')

@login_required(login_url = 'login')
def statistics(request):
    return render(request, 'statistics.html')

def choice(request):
    return render(request, 'choice.html')

@login_required(login_url = 'login')
def results(request):
    return render(request, 'results.html')