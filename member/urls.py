from django.urls import path
from . import views

urlpatterns=[
    path('registration/',views.add_member,name='add_member'),
    path('coins/',views.coin_manage,name='coin_manage'),
    path('add/staff/',views.add_staff,name='add_staff'),
]