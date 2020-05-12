from django.contrib import admin
from .models import Table,Dish,Category,Kot,Order,KotItem

admin.site.register(Table);
admin.site.register(Dish);
admin.site.register(Category);
admin.site.register(Kot)
admin.site.register(KotItem)
admin.site.register(Order)
# Register your models here.
