from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse


def Menu(request):
    return render(request,'index.html')

def MenuRouter(request):
    choice = request.POST['MenuChoice']

    if choice == '1':
        
        return render(request,'SignUp.html')