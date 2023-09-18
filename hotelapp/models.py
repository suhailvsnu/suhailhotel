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
    status=models.CharField(max_length=200,null=True)
    class Meta:
        db_table="tbl_user"







