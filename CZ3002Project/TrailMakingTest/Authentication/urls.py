from django.urls import path
from . import views

urlpatterns = [
    # home page should be login page?
    path('', views.home, name='home'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register')
]