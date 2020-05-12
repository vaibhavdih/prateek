"""prateek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from member import views
from menu import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/',include('member.urls')),
    path('menu/',include('menu.urls')),
    path('login/',views.staff_login,name="staff_login"),
    path('logout/',views.staff_logout,name="staff_logout"),
    path('captain/',views.captain,name="captain"),
    path('captain/checkin/',views.checkin,name="checkin"),
    path('captain/punch/',v.punch_kot,name="punch_kot"),
    path('kitchen/',v.kitchen,name="kitchen"),
    path('bar/',v.bar,name='bar'),
    path('waiter/',v.waiter,name="waiter"),
]
