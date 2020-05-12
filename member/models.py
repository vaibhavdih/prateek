from django.db import models
from datetime import date
from django.db.models.signals import pre_save
from django_base64field.fields import Base64Field
from .utils import member_id_generator
from django.contrib.auth.models import User

class Members(models.Model):
    IDS=(('Passport','Passport'),('Aadhar Card','Aadhar Card'),('Voter ID','Voter ID'),('Driving License','Driving License'))
    member_id = models.CharField(max_length=20,default="PM0000")
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length =20)
    contact_no = models.CharField(max_length=15)
    id_type=models.CharField(max_length=25, choices= IDS)
    id_number = models.CharField(max_length=25)
    address = models.TextField()
    registration_date = models.DateField(default =date.today)
    rating = models.IntegerField(default=1)
    pic=Base64Field()


    def __str__(self):
        return self.member_id


def pre_save_create_member_id(sender,instance,*args, **kwargs):
    instance.member_id = member_id_generator(instance)
pre_save.connect(pre_save_create_member_id,sender =Members)

class TotalCoins(models.Model):
    r10000 = models.IntegerField(default=0)
    r5000 = models.IntegerField(default=0)
    r2000 = models.IntegerField(default=0)
    r1000 = models.IntegerField(default=0)
    r500 = models.IntegerField(default=0)
    r100 = models.IntegerField(default=0)
    r50 = models.IntegerField(default=0)

class MemberCoins(models.Model):
    member_id = models.ForeignKey(Members,on_delete=models.PROTECT)
    transaction_date = models.DateField(default=date.today)
    transaction_time = models.TimeField(auto_now_add=True)
    amount= models.IntegerField(default=0)
    r10000 = models.IntegerField(default=0)
    r5000 = models.IntegerField(default=0)
    r2000 = models.IntegerField(default=0)
    r1000 = models.IntegerField(default=0)
    r500 = models.IntegerField(default=0)
    r100 = models.IntegerField(default=0)
    r50 = models.IntegerField(default=0)

class CashIn(models.Model):
	transaction_date = models.DateField(default=date.today)
	transaction_time = models.TimeField(auto_now_add=True)
	amount= models.IntegerField(default=0)
	r10000 = models.IntegerField(default=0)
	r5000 = models.IntegerField(default=0)
	r2000 = models.IntegerField(default=0)
	r1000 = models.IntegerField(default=0)
	r500 = models.IntegerField(default=0)
	r100 = models.IntegerField(default=0)
	r50 = models.IntegerField(default=0)

class Staff(models.Model):
    staff_user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    post = models.CharField(max_length=25)

class Checkin(models.Model):
	checkin_id = models.AutoField(primary_key=True)
	member_id = models.ForeignKey(Members,on_delete=models.PROTECT)
	table_id = models.ForeignKey('menu.Table', on_delete=models.PROTECT,related_name='tables')
	checkout = models.BooleanField(default=False)
	date = models.DateField(default =date.today)
	time = models.TimeField(auto_now_add =True)
