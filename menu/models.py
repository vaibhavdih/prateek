from django.db import models

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

# Create your models here.
