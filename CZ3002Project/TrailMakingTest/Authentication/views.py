from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from Authentication.models import Profile
# Create your views here.
from .decorators import  UnauthenticatedUser
from .forms import CreatUserForm, ProfileForm
# Takes a request and returns a response (request handler)


@UnauthenticatedUser
def LoginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, "Username or password is incorrect")
            

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@UnauthenticatedUser
def RegisterPage(request):
    
    if request.method == "POST":
        form = CreatUserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            # profile.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request, f'Account successfully created for {username}')
            return redirect('login')
    else:
        form = CreatUserForm()
        profile_form = ProfileForm()
    context = {'form':form, 'profile_form':profile_form}
    return render(request,'register.html', context)