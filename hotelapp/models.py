from django.db import models

# Create your models here.
class tbl_user(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    email=models.CharField(max_length=300)
    phone=models.IntegerField()
    adress=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    userimage=models.CharField(max_length=500)
    image=models.CharField(max_length=500)
    username=models.CharField(max_length=200)
    status=models.CharField(max_length=200,default="active")
    class Meta:
        db_table="tbl_user"

class tbl_resturant(models.Model):
     firstname=models.CharField(max_length=200)
     lastname=models.CharField(max_length=200)
     username=models.CharField(max_length=200)
     resturantname=models.CharField(max_length=200)
     location=models.CharField(max_length=200)
     authorizedperson=models.CharField(max_length=200)
     phone=models.IntegerField()
     type=models.CharField(max_length=200)
     email=models.CharField(max_length=200)
     staff=models.IntegerField()
     image=models.CharField(max_length=200)
     status=models.CharField(max_length=200,null=True)

     class Meta:
         db_table="tbl_resturant"

class tbl_accounts(models.Model):


  username=models.CharField(max_length=200)
  email=models.CharField(max_length=200)
  accounttype=models.CharField(max_length=200)

  class Meta:
        db_table="tbl_accounts"
class tbl_foodMenu(models.Model):
    restname=models.CharField(max_length=30)
    menuname=models.CharField(max_length=30)
    cusine=models.CharField(max_length=30)
    origin=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
   
    class Meta:
        db_table="tbl_foodMenu"      

class fooditem(models.Model):
    RestaurantName=models.CharField(max_length=30)
    MenuName=models.CharField(max_length=30)
    MenuItemName=models.CharField(max_length=30)
    Quantity=models.IntegerField()
    price=models.IntegerField()
    cookingtime=models.CharField(max_length=30)
    status=models.CharField(max_length=30,default="available")
    type=models.CharField(max_length=30)
    class Meta:
        db_table="fooditem"    

class offer(models.Model):
    
    MenuItemName=models.CharField(max_length=30)
    offer=models.CharField(max_length=30)
    startdate=models.CharField(max_length=30)
    enddate=models.CharField(max_length=30)
    details=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    class Meta:
        db_table="offer"          

class tbl_cart(models.Model):
    username=models.CharField(max_length=200)
    MenuItemName=models.CharField(max_length=30)
    resturantname=models.CharField(max_length=200)
    quantity=models.IntegerField()
    price=models.IntegerField()
    totalamount=models.IntegerField()
    image=models.CharField(max_length=200)

    class Meta:
        db_table="tbl_cart"






















