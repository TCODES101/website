from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class property(models.Model):

    name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)

class money(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=20,default='')
    desc=models.CharField(max_length=20,default='Rent')
    amount=models.IntegerField()
    date=models.CharField(max_length=20, default='')  


    def __str__(self):
        return self.name
class bedsitter(models.Model):
    room=models.CharField(max_length=20,default='Bedsitter')
    available=models.IntegerField()
    def __str__(self):
        return self.room
class oneBedroom(models.Model):
    room=models.CharField(max_length=20,default='OneBedroom')
    available=models.IntegerField()
    def __str__(self):
        return self.room

    

    

