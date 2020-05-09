from django.urls import path
from . import views

urlpatterns=[
    path('add/',views.add_options,name='add_options'),
path('add/table/',views.add_table,name='add_table'),
path('add/category/',views.add_category,name='add_category'),
path('add/dish/',views.add_dish,name='add_dish'),
path('order/',views.order,name='order'),



]