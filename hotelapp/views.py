from django.shortcuts import render,redirect
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')
def login (request):
    return render(request,'login.html')
def createaccount(request):
    return render(request,'createaccount.html')
def userlogin(request):
    return render(request,'userhomepage.html')
    