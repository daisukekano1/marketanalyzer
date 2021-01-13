from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import datetime
import json
from urllib.request import urlopen
from app.lib import *

def home(request):
    template = loader.get_template('app/main_home.html')
    data = []
    return HttpResponse(template.render({"data": data}, request))

def getQuote(request):
    data = []
    ticker = request.GET.get("ticker")
    data = get_quote(ticker)
    return JsonResponse({"data": data})

