from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

from .forms import CreatUserForm
# Takes a request and returns a response (request handler)

def home(request):
    return render(request, 'home.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('TMT_A')

    context = {}
    return render(request, 'login.html', context)

def RegisterPage(request):
    form = CreatUserForm()
    if request.method == "POST":
        form = CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created for '+ form.cleaned_data.get('username'))
            return redirect('login')
    context = {'form':form}
    return render(request,'register.html', context)