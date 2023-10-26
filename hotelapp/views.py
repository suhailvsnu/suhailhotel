from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from hotelapp.models import tbl_user,tbl_resturant,tbl_accounts,tbl_foodMenu,fooditem,offer

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

def viewuser(request):
     a = request.session['username']
     c=tbl_user.objects.get (username=a)
     return render (request,'viewuser.html',{'data':c})

def updateuser1(request):
     

     a = request.session['username']
     c=tbl_user.objects.get (username=a)
     return render(request,'updateuserview.html',{'data':c})
def updateuser2(request,id):
        d=tbl_user.objects.get(id=id)
        return render(request,'updateuser.html',{'x':d})


def updateuser3(request,id):
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
    a=request.session['username']

    return render(request,'foodmenu.html',{'data':a})
def addfoodmenu(request):
   
    d=tbl_foodMenu()
    d.restname=request.POST.get('rname') 
    d.menuname=request.POST.get('mname')
    d.cusine=request.POST.get('cusine')   
    d.origin=request.POST.get('orgin')
    d.status=request.POST.get('status')
    d.save()
    return redirect('/hotelhomepage/')

def viewfood(request):
     b=tbl_foodMenu.objects.all()
     return render(request,'viewfood.html',{'data':b})
def viewhotelprofile(request):
     a = request.session['username']
     c=tbl_resturant.objects.get (username=a)

     return render(request,'viewrestprofile.html',{'data':c})
def addmenu(request):
    a = request.session['username']
    b=tbl_foodMenu.objects.filter(restname=a)

    return render(request,'addmenuitem.html',{'data':a,"data1":b})
def updatehotel1(request):
    a=tbl_resturant.objects.all()
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
def addoffer(request):
    a = request.session['username']
    b=tbl_foodMenu.objects.filter(restname=a)

    return render(request,'addoffer.html',{'data':a,"data1":b,"data1":b})

def  addofferform(request):
    p1=offer()
   

    p1.MenuItemName=request.POST.get('MenuItemName')
    p1.offer=request.POST.get('offer')
    p1.startdate=request.POST.get('startdate')
    p1.enddate=request.POST.get('enddate')
    p1.details=request.POST.get('details')
    p1.status=request.POST.get('status')
    p1.save()
    return redirect('/viewhotel/')
def viewfoodmenuitem(request):
     b=fooditem.objects.all()
     return render(request,'viewfoodmenuitem.html',{'data':b})
def viewoffer(request):
    b=offer.objects.all()
    return render(request,'viewoffer.html',{'data':b})
def upddelfoodmenu(request):
    b=tbl_foodMenu.objects.all()
    return render(request,'upddelfoodmenu.html',{'data':b})
def deletefoodmenu(request,id):
    b=tbl_foodMenu.objects.get(id=id)
    b.delete()
    return redirect('/delupfoodmenu/')   
def updatefoodmenu1(request):
    b=tbl_foodMenu.objects.all()
    return render(request,'updatefoodmenuview.html',{'data':b})
def updatefoodmenu2(request,id):
    a=tbl_foodMenu.objects.get(id=id)
    b=tbl_foodMenu.objects.filter(restname=a)

    return render(request,'updatefoodmenu2.html',{'x':a})
def updatefoodmenu3(request,id):
    a=tbl_foodMenu.objects.get(id=id)
    a.restname=request.POST.get('rname') 
    a.menuname=request.POST.get('mname')
    a.type=request.POST.get('type')
    a.cusine=request.POST.get('cusine')   
    a.origin=request.POST.get('orgin') 
    a.save()

    return redirect('/delupfoodmenu/')
def delupfooditem(request):
    b=fooditem.objects.all()
    return render(request,'updatedeletefooditem.html',{'data':b})
def delfooditem(request,id):
    b=fooditem.objects.get(id=id)
    b.delete()
    return redirect('/delupitem/')
def updatefooditem1(request):
    b=fooditem.objects.all()
    return render(request,'updatefoodview.html',{'data':b})
def updatefooditem2(request,id):
    b=fooditem.objects.get(id=id)
    return render(request,'updatefooditem2.html',{'x':b})

def delupoffer(request):
     b=offer.objects.all()
     return render(request,'delupoffer.html',{'data':b})
def deleteoffer(request,id):
    b=offer.objects.get(id=id)
    b.delete()
    return redirect('/delupoffer/')
def updateoffer1(request):
    b=offer.objects.all()
    return render(request,'updateofferview.html',{'data':b})
def updateoffer2(request,id):
    a = request.session['username']

    b=tbl_foodMenu.objects.filter(restname=a)
    c=offer.objects.get(id=id)


    return render(request,'updateoffer.html',{'data':a,'data1':b,'x':c})
def updateoffer3(request,id):
    p1=offer.objects.get(id=id)
   

    p1.MenuItemName=request.POST.get('MenuItemName')
    p1.offer=request.POST.get('offer')
    p1.startdate=request.POST.get('startdate')
    p1.enddate=request.POST.get('enddate')
    p1.details=request.POST.get('details')
    p1.status=request.POST.get('status')
    p1.save()
    return redirect('/delupoffer/')
def viewresthome(request):
     b=tbl_resturant.objects.all()
     return render(request,'viewresthome.html',{'data':b})
def viewofferhome(request):
     b=offer.objects.all()
     return render(request,'viewofferhome.html',{'data':b})
def addfooditem(request):
 c=fooditem()    
 c.restaurantName=request.POST.get('rname')  
 c.menuName= request.POST.get('mname')  
 c.menuItemName=request.POST.get('mitem')  
 c.type=request.POST.get('type')  
 c.quantity=request.POST.get('qantity')  
 c.price=request.POST.get('prize')  
 c.cookingtime=request.POST.get('cookingtime')  
 c.status=request.POST.get('status')  

 c.save()
 return redirect('/hotelhomepage/')
def viewuserfoodmenu(request,id):
    a=tbl_resturant.objects.get(id=id)
    b=tbl_foodMenu.objects.filter(restname=a.username)
    return render(request,'viewuserfoodmenu.html',{'data':b})
def viewmenuitem(request,id):
        a=tbl_foodMenu.objects.get(id=id)
        b=fooditem.objects.filter(menuName=a.menuname)
        return render(request,'viewfooditemuser.html',{'data':b})







    













 
        












    
  










