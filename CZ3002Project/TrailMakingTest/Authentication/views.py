from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from Authentication.models import Profile
# Create your views here.
from .decorators import AllowedUsers, UnauthenticatedUser
from .forms import CreatUserForm
from django.contrib.auth.models import Group
# Takes a request and returns a response (request handler)


@UnauthenticatedUser
def LoginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            messages.info(request, "Username or password is incorrect")
            

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@UnauthenticatedUser
def RegisterPage(request):
    
    form = CreatUserForm()
    if request.method == "POST":
        form = CreatUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name = 'Profile')
            user.groups.add(group)
            Profile.objects.create(
                user=user,
            )
            messages.success(request, 'Account successfully created for ', username)
            return redirect('login')
    context = {'form':form}
    return render(request,'register.html', context)