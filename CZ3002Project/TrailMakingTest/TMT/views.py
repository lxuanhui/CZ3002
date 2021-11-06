from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Authentication.models import Profile, Attempts
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required(login_url = 'login')
def home(request):
    return render(request, 'home.html')
    
@login_required(login_url = 'login')
def TMTA(request):
    return render(request, 'TMTA.html')

@login_required(login_url = 'login')
def TMTB(request):
    return render(request,'TMTB.html')

@login_required(login_url = 'login')
def statistics(request):
    return render(request, 'statistics.html')

@login_required(login_url = 'login')
def choice(request):
    return render(request, 'choice.html')


@login_required(login_url = 'login')
def results(request):
    if request.method == "POST" and request.is_ajax():
        print("POST WORKS")
        request_data = request.POST
        print(request_data)
        data_dict = request_data.dict()
        totalTime = data_dict['timeToComplete']
        errors = data_dict['numOfErrors']
        print(totalTime)
        print(errors)
        
        # errorPerSec = errors / totalTime
        # # 15 is number of buttons
        # errorPencentage = errors/15
        # current_user = request.user
        # attempt = Attempts()
        # attempt.user = current_user
        # attempt.timeToComplete = totalTime
        # attempt.numOfErrors = errors
        # attempt.errorPerSec = errorPerSec
        # attempt.errorPencentage = errorPencentage
        # attempt.save()
        return  HttpResponse("Okay") 
    context = {}
    return render(request, 'results.html', context)

@login_required
def statistics(request):
            

    return render(request, 'statistics.html')