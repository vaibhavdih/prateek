from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , HttpResponseNotFound
from .models import Table,Dish,Category

def add_options(request):
    if request.method=='GET':
        a=Category.objects.all()
        return render(request,'add.html',{"categories":a})

@csrf_exempt
def add_table(request):
    if request.method=='POST':
        if len(Table.objects.filter(table_id=request.POST['table_id']))!=0:
            return HttpResponse(0)
        else:
            a=Table.objects.create(table_id=request.POST['table_id'],capacity=request.POST['capacity'],service_id=request.POST['sc'])
            return HttpResponse(1)

@csrf_exempt
def add_category(request):
    if request.method=='POST':
        if len(Category.objects.filter(name=request.POST['cat_name']))!=0:
            return HttpResponse(0)
        else:
            a=Category.objects.create(name=request.POST['cat_name'],type=request.POST['cat_type'])
            return HttpResponse(1)


@csrf_exempt
def add_dish(request):
    if request.method == 'POST':
        print(request.POST)
        if len(Dish.objects.filter(name=request.POST['name'])) != 0:
            return HttpResponse(0)
        else:
            b=Category.objects.filter(name=request.POST['category'])[0]
            a = Dish.objects.create(name=request.POST['name'],category=b,coins=request.POST['coins'],description=request.POST['description'])
            return HttpResponse(1)

@csrf_exempt
def order(request):
    if request.method=="GET":
        a=Category.objects.all()
        return render(request,"order.html",{"categories":a})