from django.urls import path
from . import views

urlpatterns = [
    path('SignUp/', views.SignUp),
    path('SignUp/SaveUsername/', views.SaveUsername),
    path('SignIn/', views.SignIn),
    path('SignIn/CheckSignIn/', views.CheckSignIn),
    path('Inside/', views.Inside),
    path('Inside/DepositMoney/', views.DepositMoney),
    path('Inside/DepositMoney/AddMoneytoModel/', views.AddMoneytoModel),
    path('Inside/Buy2/', views.Buy2),
    path('Inside/Buy3/', views.Buy3),
    path('Inside/Buy4/', views.Buy4),
    path('Inside/Buy5/', views.Buy5),
    path('Inside/ViewPurchases/', views.ViewPurchases),
    path('Inside/ViewPurchases/BackInside/', views.BackInside)
    ]