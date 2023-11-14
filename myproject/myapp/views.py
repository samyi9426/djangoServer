from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect

def hello(request):
        return HttpResponse("Hello, Django! im")

def index(request):
        return HttpResponse("<html><body><h1>Hello, Django!</h1></body></html>")

def api_a(request):
        data = {"name": "zhongxm", "age": 18, "address": "beijing", "gender": "male"}
        return JsonResponse(data)
