from django.urls import path, re_path, include
from app import views_main

urlpatterns = [
    # The main page functions
    path('', views_main.home, name='home'),
    path('getQuote', views_main.getQuote, name='getQuote')

]
