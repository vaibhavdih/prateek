from django.db import models
from member.models import Members,Staff
from datetime import date

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    type = models.CharField(max_length=20)


class Dish(models.Model):
	dish_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length= 50)
	coins = models.IntegerField()
	description = models.CharField(max_length=50,default="")
	category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='dish')

	def __str__(self):
		return self.name

class Table(models.Model):
	table_id = models.CharField(max_length=15)
	service_id = models.CharField(max_length=20)
	capacity = models.IntegerField()
	status = models.CharField(default="vacant", max_length=20)

	def __str__(self):
		return self.table_id


class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	member_id = models.ForeignKey(Members,on_delete=models.PROTECT)
	staff_id = models.ForeignKey(Staff, on_delete = models.PROTECT)
	table_id = models.ForeignKey(Table, on_delete = models.PROTECT)
	order_date = models.DateField(default =date.today)
	order_time = models.TimeField(auto_now_add =True)
	amount = models.FloatField(default=0)

class Kot(models.Model):
	STATUS=(('Waiting','Waiting'),('Cooking','Cooking'),('Delivered','Delivered'))
	kot_id = models.AutoField(primary_key=True)
	member_id = models.ForeignKey(Members,on_delete=models.PROTECT)
	staff_id = models.ForeignKey(Staff, on_delete = models.PROTECT)
	table_id = models.ForeignKey(Table, on_delete = models.PROTECT)
	order_date = models.DateField(default =date.today)
	order_time = models.TimeField(auto_now_add =True)
	order_id = models.ForeignKey(Order, on_delete = models.PROTECT)
	status=models.CharField(max_length=15,default='Waiting')
	amount = models.FloatField()

class KotItem(models.Model):
	STATUS = (('Waiting', 'Waiting'), ('Cooking','Cooking'),('Cooked', 'Cooked'), ('Delivered', 'Delivered'))
	kotitem_id = models.AutoField(primary_key=True)
	kot_id = models.ForeignKey(Kot, on_delete = models.PROTECT, related_name='items')
	quantity = models.IntegerField(default =1)
	dish_id = models.ForeignKey(Dish, on_delete = models.PROTECT)
	status =models.CharField(max_length=15,default="Waiting")
	category_type = models.CharField(max_length=20)