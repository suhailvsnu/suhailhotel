from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from hotelapp.models import tbl_user,tbl_resturant,tbl_accounts,tbl_foodMenu

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return render(request,'demo.html')
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
    e=tbl_accounts()
    e.username=request.POST.get('username')
    e.email=request.POST.get('email')
    e.accounttype="user"

    d.username=request.POST.get('username') 
    d.firstname=request.POST.get('firstname')
    d.lastname=request.POST.get('lastname')
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
    e.save()
    return redirect('/login/')
def signup(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    data=authenticate(username=username,password=password)
    request.session['username']=username
    if data is not None and data.is_superuser==1:
            return redirect('/admin1/') 
    
    
    elif data is not None and data.is_superuser == 0:
       a=tbl_accounts.objects.get(username=data)
       if a.accounttype=="user":
            return redirect('/user1/')
       elif a.accounttype=="resturant":
           return redirect('/hotelhomepage/')
       else:
    
           pass
    else:
       return HttpResponse('User not Exist')   
    

      
      
      
           
      
    
def user1(request):
    a=request.session['username']
    c=tbl_user.objects.get(username=a)
    
    
    return render (request,'userhomepage.html',{'item':c})     

def admin1(request):
    a=request.session['username']

    return render(request,'adminpage.html') 
def addhotel(request):
    return render(request,'addhotel.html')
def hotelinput(request):
    c=User()
    d=tbl_resturant()
    e=tbl_accounts()
    e.username=request.POST.get('username')
    e.email=request.POST.get('email')
    e.accounttype="resturant"

    d.username=request.POST.get('username')
    d.firstname=request.POST.get('firstname')
    d.lastname=request.POST.get('lastname')
    d.resturantname=request.POST.get('rname')
    d.location=request.POST.get('location')
    d.authorizedperson=request.POST.get('atperson')
    d.phone=request.POST.get('phone')
    d.type=request.POST.get('type')
    d.email=request.POST.get('email')
    d.staff=request.POST.get('staff')
    photo=request.FILES['image'] 
    fs= FileSystemStorage()
    filename=fs.save(photo.name,photo) 
    uploaded_file_url=fs.url(filename)
    d.image=uploaded_file_url
    password=request.POST.get('password')
    c.set_password(password)
    c.username=request.POST.get('username')
    c.email=request.POST.get('email')
    d.save()
    c.save()
    e.save()
    return redirect('/admin1/')
def viewhotel(request):
     b=tbl_resturant.objects.all()
     return render(request,'viewhotel.html',{'data':b})
def removehotel(request):
     b=tbl_resturant.objects.all()
     return render(request,'deletehotel.html',{'data':b})
def delhotel(request,id):
    a=tbl_resturant.objects.get(id=id)
    a.delete()
    return redirect('/removehotel/')
def hotelhomepage(request):
    a=request.session['username']
    c=tbl_resturant.objects.get(username=a)
    return render(request,'hotelhomepage.html',{'item':c})
def updatehotel1(request):
    a=tbl_resturant.objects.all()
    # return render(request,'updatehotel.html',{'x':a})
    return render(request,'updateRestView.html',{'data':a})
def updtRest2(request,id):
     a=tbl_resturant.objects.get(id=id)
     return render(request,'updatehotel.html',{'x':a})
def updatehotel2(request,id):
 a=tbl_resturant.objects.get(id=id)
 try:
     a.username=request.POST.get('username')   

     a.firstname=request.POST.get('firstname')
     a.lastname=request.POST.get('lastname')
     a.resturantname=request.POST.get('rname')
     a.location=request.POST.get('location')
     a.authorizedperson=request.POST.get('atperson')
     a.phone=request.POST.get('phone')
     a.type=request.POST.get('type')
     a.email=request.POST.get('email')
     a.staff=request.POST.get('staff')
     photo=request.FILES['image']
     fs= FileSystemStorage()
     filename=fs.save(photo.name,photo) 
     uploaded_file_url=fs.url(filename)
     a.image=uploaded_file_url


     a.save()
 except: 
        a.username=request.POST.get('username')   
        a.firstname=request.POST.get('firstname')
        a.lastname=request.POST.get('lastname')
        a.resturantname=request.POST.get('rname')
        a.location=request.POST.get('location')
        a.authorizedperson=request.POST.get('atperson')
        a.phone=request.POST.get('phone')
        a.type=request.POST.get('type')
        a.email=request.POST.get('email')
        a.staff=request.POST.get('staff')
        a.save()
        
 return redirect('/viewhotel/')
def viewuser(request):
     a = request.session['username']
     c=tbl_user.objects.get (username=a)
     return render (request,'viewuser.html',{'data':c})
def updateuser1(request,id):
    d=tbl_user.objects.get(id=id)
    return render(request,'updateuser.html',{'x':d})
def updateuser2(request,id):
 d=tbl_user.objects.get(id=id)   

 try: 
    d.username=request.POST.get('username') 
    d.firstname=request.POST.get('firstname')
    d.lastname=request.POST.get('lastname')
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
   
    d.save()
 except:
    d.username=request.POST.get('username') 
    d.firstname=request.POST.get('firstname')
    d.lastname=request.POST.get('lastname')
    d.email=request.POST.get('email')
    d.gender=request.POST.get('gender') 
    d.phone=request.POST.get('phone')
    d.adress=request.POST.get('adress')
    d.district=request.POST.get('district')
    d.save()

    return redirect('/userview/')
 
def addfood(request):
    return render(request,'foodmenu.html')
def addfoodmenu(request):
    c=tbl_foodMenu()
    c.restname=request.POST.get('rname') 
    c.menuname=request.POST.get('mname')
    c.type=request.POST.get('type')
    c.cusine=request.POST.get('cusine')   
    c.origin=request.POST.get('orgin') 
    c.save()
    return redirect('/hotelhomepage/')

def viewfood(request):
    c=tbl_foodMenu.objects.all()
    return render(request,'viewfood.html',{'data':c})
def viewhotelprofile(request):
     a = request.session['username']
     c=tbl_resturant.objects.get (username=a)

     return render(request,'viewrestprofile.html',{'data':c})




    
  










