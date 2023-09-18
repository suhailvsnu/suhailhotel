from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from hotelapp.models import tbl_user
# Create your views here.
def index(request):
    return render(request,'index.html')
    # return render(request,'adminpg.html')
    # return render(request,'userhomepage.html')
    # return render(request,'hotelpage.html')

def login (request):
    return render(request,'login.html')
def createaccount(request):
    return render(request,'createaccount.html')
def userlogin(request):
    return render(request,'userhomepage.html')
def userinput(request):
    c=User()
    d=tbl_user()

    d.username=request.POST.get('username') 
    d.firstname=request.POST.get('firstname')
    d.email=request.POST.get('email')
    d.gender=request.POST.get('gender') 
    d.phone=request.POST.get('phone')
    d.adress=request.POST.get('adress')
    d.district=request.POST.get('district')
    photo=request.FILES['image'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    d.image=uploaded_file_url
    c.username=request.POST.get('username')
    c.email=request.POST.get('email')
    password=request.POST.get('password')
    c.set_password(password)
    c.save()
    d.save()
    return redirect('/')
def signup(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    data=authenticate(username=username,password=password)
    request.session['username']=username
    if data is not None and data.is_superuser==1:
            return redirect('/admin1/') 
    elif data is not None and data.is_superuser == 0:
       return redirect('/user1/')
    else:
       return HttpResponse('User not Exist')
def user1(request):
    a=request.session['username']
    c=tbl_user.objects.get(username=a)
    
    
    return render (request,'userhomepage.html')     

def admin1(request):
    a=request.session['username']

    return render(request,'adminpage.html') 