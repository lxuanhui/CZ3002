from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('choice/', views.choice, name='choice'),
    path('results/', views.results, name='results'),
    path('TMTA/', views.TMTA, name='TMTA'),
    path('TMTB/', views.TMTB, name ='TMTB'),
    path('statistics/', views.statistics, name = 'statistics')
    
]