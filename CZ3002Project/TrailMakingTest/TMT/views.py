from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from Authentication.decorators import AllowedUsers
# Create your views here.

@login_required(login_url = 'login')
def home(request):
    return render(request, 'Home.html')

@login_required(login_url = 'login')
def TMT_A(request):
    return render(request,"TMT_A.html")

@login_required(login_url = 'login')
def TMT_B(request):
    return render(request,'TMT_B.html')

@login_required(login_url = 'login')
def statistics(request):
    return render(request, 'statistics.html')