from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , HttpResponseNotFound
from .models import Table,Dish,Category,Order,KotItem,Kot
from member.models import Checkin,Staff
from django.db.models import Q

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
        b=Table.objects.filter(status="occupied")
        return render(request,"order.html",{"categories":a,"tables":b})
    else:
        data = request.POST.get('data')
        table_id = request.POST.get('table')
        table_ob = Table.objects.filter(table_id=table_id)[0]
        user_ = request.user
        print(user_)
        staff_ob=Staff.objects.filter(staff_user=user_)[0]
        order_ob = Order.objects.filter(table_id=table_ob).filter(amount=0)[0]
        checkin_ob = Checkin.objects.filter(table_id=table_ob).filter(checkout=False)[0]
        member_ob = checkin_ob.member_id
        kot = Kot.objects.create(member_id=member_ob, table_id=table_ob, staff_id=staff_ob, order_id=order_ob, amount=0)

        price = 0
        for i in data.split(";")[:-1]:
            dish_name = (i.split("=")[0])
            quantity = int(i.split("=")[1])
            dish_ob = Dish.objects.filter(name=dish_name)[0]
            kot_item = KotItem.objects.create(quantity=quantity, dish_id=dish_ob, kot_id=kot,category_type=dish_ob.category.type)
            price = price + (quantity * dish_ob.coins)
        kot.amount = price
        kot.save()

        print(request.POST)
        return HttpResponse("you")


@csrf_exempt
def punch_kot(request):
    if request.method=="POST":
        kot_id = int(request.POST.get('kot_id'))
        kot=Kot.objects.filter(kot_id=kot_id)[0]
        kot.status='Cooking'
        kot.save()
        return redirect('/captain/punch/')
    else:
        kots = Kot.objects.filter(status='Waiting')
        key=1
        if len(kots) ==0:
            key=0
        return render(request,"kot_punch.html",{"kots":kots,"key":key})

@csrf_exempt
def kitchen(request):
    if request.method=='GET':
        kots=[]
        kot=Kot.objects.filter(Q(status='Cooking') | Q(status='LiquorCooked'))
        for kot_ in kot:
            if len(kot_.items.filter(category_type='Food'))!=0:
                kots.append(kot_)

        key=1
        if len(kots)==0:
            key=0
        return render(request,"kitchen.html",{"kots":kots,"key":key})
    else:
        kotitem_id =int(request.POST.get('kotitem_id'))
        print(kotitem_id)
        kotitem = KotItem.objects.filter(kotitem_id=kotitem_id)[0]
        kotitem.status='Cooked'
        kotitem.save()
        kot_ob = kotitem.kot_id
        total = len(kot_ob.items.filter(category_type='Food'))
        cooked = len(kot_ob.items.filter(category_type='Food').filter(status='Cooked'))
        if total == cooked:
            total_liquor = len(kot_ob.items.filter(category_type='Liquor'))
            cooked_liquor = len(kot_ob.items.filter(category_type='Liquor').filter(status='Cooked'))
            if total_liquor == cooked_liquor:
                kot_ob.status ='Cooked'
            else:
                kot_ob.status='FoodCooked'
            kot_ob.save()

        return redirect('/kitchen/')

@csrf_exempt
def bar(request):
    if request.method=='GET':
        kots=[]
        kot=Kot.objects.filter(Q(status='Cooking') | Q(status='FoodCooked'))
        for kot_ in kot:
            if len(kot_.items.filter(category_type='Liquor'))!=0:
                kots.append(kot_)

        key=1
        if len(kots)==0:
            key=0
        return render(request,"bar.html",{"kots":kots,"key":key})
    else:
        kotitem_id =int(request.POST.get('kotitem_id'))
        print(kotitem_id)
        kotitem = KotItem.objects.filter(kotitem_id=kotitem_id)[0]
        kotitem.status='Cooked'
        kotitem.save()
        kot_ob = kotitem.kot_id
        total = len(kot_ob.items.filter(category_type='Liquor'))
        cooked = len(kot_ob.items.filter(category_type='Liquor').filter(status='Cooked'))
        if total == cooked:
            total_food = len(kot_ob.items.filter(category_type='Food'))
            cooked_food = len(kot_ob.items.filter(category_type='Food').filter(status='Cooked'))
            if total_food == cooked_food:
                kot_ob.status = 'Cooked'
            else:
                kot_ob.status = 'LiquorCooked'
            kot_ob.save()

        return redirect('/bar/')

@csrf_exempt
def waiter(request):
    if request.method=='GET':
        a=KotItem.objects.filter(status="Cooked")
        return render(request,'waiter.html',{"kotitems":a})
    else:
        print(request.POST)
        b=int(request.POST.get('kotitem_id'))
        kotitem = KotItem.objects.filter(kotitem_id=b)[0]
        kotitem.status='Delivered'
        kotitem.save()
        return redirect('/waiter/')



