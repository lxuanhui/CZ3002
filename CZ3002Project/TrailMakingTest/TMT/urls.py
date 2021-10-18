from django.urls import path
from . import views

urlpatterns = [
    
    path('TMT_A/', views.TMT_A, name='TMT_A'),
    path('TMT_B/', views.TMT_B, name ='TMT_B')
    
]