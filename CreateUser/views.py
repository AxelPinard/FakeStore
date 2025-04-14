#from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

Users = []

def SignUp(request):
    return render(request, 'SignUp.html')

def SignIn(request):
    return render(request, 'SignIn.html')

def CheckSignIn(request):
    name = request.POST['username']
    for user in Users:
        if name == user.UserName:
            return redirect('/CreateUser/Inside/')
    return redirect('/')

def SaveUsername(request):
    name = request.POST['username']
    for user in Users:
        if name == user.UserName:
            return redirect('/')
    p1 = User()
    Users.append(p1)
    Users[-1].UserName = request.POST['username']
    Users[-1].money = 0
    Users[-1].Purchases = ''

    return redirect('/')

def Inside(request):
    return render(request, 'Inside.html',{'Person':Users[-1]})

def DepositMoney(request):
    return render(request, 'Deposit.html')

def AddMoneytoModel(request):
    Users[-1].money += int(request.POST['money'])
    return redirect('/CreateUser/Inside/')

def Buy2(request):
    Users[-1].money -= 5
    Users[-1].Purchases += 'Brothers.jpeg '
    return redirect('/CreateUser/Inside/')

def Buy3(request):
    Users[-1].money -= 7
    Users[-1].Purchases += 'Cat.gif '
    return redirect('/CreateUser/Inside/')

def Buy4(request):
    Users[-1].money -= 4
    Users[-1].Purchases += 'LISTENHERE.jpeg '
    return redirect('/CreateUser/Inside/')

def Buy5(request):
    Users[-1].money -= 6
    Users[-1].Purchases += 'SpongeBobYEESS.gif '
    return redirect('/CreateUser/Inside/')

def ViewPurchases(request):
    return render(request, 'Cart.html', {'Person':Users[-1]})

def BackInside(request):
    return redirect('/CreateUser/Inside/')

