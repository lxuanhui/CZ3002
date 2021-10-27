from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('choice/', views.choice, name='choice'),
    path('results/', views.results, name='results'),
    path('TMTA/', views.TMT_A, name='TMTA'),
    path('TMTB/', views.TMT_B, name ='TMTB'),
    path('statistics/', views.statistics, name = 'statistics')
    
]