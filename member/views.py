from django.shortcuts import render,redirect
from .models import Members,MemberCoins, TotalCoins, CashIn, Staff,Checkin
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from menu.models import Table,Order


@csrf_exempt
def add_member(request):
    if request.method=='POST':
        print("====================================================================")
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        address=request.POST["address"]
        contact=request.POST["contact"]
        id_no=request.POST["id_no"]
        id_type=request.POST["id_type"]
        rating=request.POST["rating"]
        pic=request.POST["pic"]
        print("log received")
        a=Members.objects.create(first_name=fname,last_name=lname,address=address,contact_no=contact,rating=int(rating),id_number=id_no,id_type=id_type,pic=pic)
        return HttpResponse(a.member_id)
    else:
        return render(request,'new.html')

@csrf_exempt
def add_staff(request):
    if request.method=='GET':
        print(request.user)
        return render(request,"add_staff.html")
    else:
        fname=request.POST['fname']
        lname = request.POST["lname"]
        contact = request.POST['contact']
        work = request.POST["work"]
        username = request.POST['username']
        password = request.POST['password']
        email = fname+lname+"@gmail.com"

        if len(User.objects.filter(username=username))!=0:
            return HttpResponse(0)
        else:
            a=User.objects.create_user(username=username,email=email,password=password)
            b=Staff.objects.create(staff_user=a, first_name=fname, last_name=lname, contact_no=contact,username=username,password=password,post=work)

            return HttpResponse(1)



@csrf_exempt
def coin_manage(request):
    if request.method=='POST':
        r10000 =int(request.POST.get("r10000"))
        r5000 = int(request.POST.get("r5000"))
        r2000 = int(request.POST.get("r2000"))
        r1000 = int(request.POST.get("r1000"))
        r500 = int(request.POST.get("r500"))
        r100 = int(request.POST.get("r100"))
        r50 = int(request.POST.get("r50"))
        amount = int(request.POST.get("amount"))
        if int(request.POST.get("key"))==1:
            mem_id = request.POST.get("mem_id")
            a=MemberCoins.objects.create(r10000=r10000,r5000=r5000,r2000=r2000,r1000=r1000,r500=r500,r100=r100,r50=r50,amount=amount,member_id=Members.objects.filter(member_id=mem_id)[0])


            if len(TotalCoins.objects.all())==0:
                b=TotalCoins.objects.create(r10000=0,r5000=0,r2000=0,r1000=0,r500=0,r100=0,r50=0)
            else:
                b=TotalCoins.objects.all()[0]


            if b.r10000>=r10000 and b.r5000>=r5000 and b.r2000>=r2000 and b.r1000>=r1000 and b.r500>=r500 and b.r100>=r100 and b.r50>=r50:
                b.r10000=b.r10000-r10000
                b.r5000=b.r5000-r5000
                b.r2000=b.r2000-r2000
                b.r1000=b.r1000-r1000
                b.r500=b.r500-r500
                b.r100=b.r100-r100
                b.r50=b.r50-r50
                b.save()
                return HttpResponse("Cash Out successful")
            else:
                return HttpResponse("Inventory Deficient and CashOut unsuccessful")


        else:
            a=CashIn.objects.create(r10000=r10000,r5000=r5000,r2000=r2000,r1000=r1000,r500=r500,r100=r100,r50=r50,amount=amount)
            if len(TotalCoins.objects.all())==0:
                b=TotalCoins.objects.create(r10000=0,r5000=0,r2000=0,r1000=0,r500=0,r100=0,r50=0)

            b = TotalCoins.objects.all()[0]
            b.r10000 = b.r10000 + r10000
            b.r5000 = b.r5000 + r5000
            b.r2000 = b.r2000 + r2000
            b.r1000 = b.r1000 + r1000
            b.r500 = b.r500 + r500
            b.r100 = b.r100 + r100
            b.r50 = b.r50 + r50
            b.save()
        return HttpResponse("CashIn successful")
    else:
        members=Members.objects.all()
        if len(TotalCoins.objects.all()) == 0:
            b = TotalCoins.objects.create(r10000=0, r5000=0, r2000=0, r1000=0, r500=0, r100=0, r50=0)
        inventory=TotalCoins.objects.all()[0]
        return render(request,'coins.html',{"members":members,"inventory":inventory})

@csrf_exempt
def staff_login(request):
    if request.method=='GET':
        print(request.user)
        key=1
        return render(request,"login.html",{"key":key})
    else:
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            ab = Staff.objects.filter(staff_user=user)[0]
            if ab.post == 'Cashier':
                return redirect("/member/registration/")
            elif ab.post == 'Captain':
                return redirect("/captain/")
            elif ab.post == 'Chef':
                return redirect("/kitchen/")
            elif ab.post == 'Bartender':
                return redirect("/bar/")
            elif ab.post == 'Waiter':
                return redirect("/waiter/")
            elif ab.post == 'Manager':
                return redirect('/menu/add/')


        else:
            return render(request,"login.html",{"key":0})

@csrf_exempt
def staff_logout(request):
    if request.method=='GET':
        logout(request)
        return redirect("/login/")


@csrf_exempt
def captain(request):
    if request.method=='GET':
        a=Table.objects.all()
        b=Members.objects.all()
        return render(request,"captain.html",{"tables":a,"memberss":b})
    else:
        if request.POST.get("table") is not None:
            a=Table.objects.filter(table_id=request.POST['table'])[0]
            c=Checkin.objects.filter(checkout=False).filter(table_id=a)[0]
            c.checkout=True
            c.save()
            a.status = "vacant"
            a.save()
            return redirect("/captain/")

@csrf_exempt
def checkin(request):
    if request.method=="POST":
        if request.POST.get('mem_one') is None:
            quantity = int(request.POST['quantity'])
            member = request.POST['member']
            b = Members.objects.all()
            a=Table.objects.filter(capacity__gte=quantity).filter(status="vacant")
            return render(request,'checkin.html',{"tables":a,"member_one":member,"quantity":quantity,"memberss":b})
        else:
            member=request.POST['mem_one']
            table=request.POST['table']
            e=Table.objects.filter(table_id=table)[0]
            user_ = request.user
            print(user_,type(user_))
            staff_ob = Staff.objects.filter(staff_user=user_)[0]
            print(staff_ob)
            d = Checkin.objects.create(member_id=Members.objects.filter(member_id=member)[0],table_id=e)
            g=Order.objects.create(member_id=Members.objects.filter(member_id=member)[0],staff_id=staff_ob,table_id=e)
            e.status = "occupied"
            e.save()
            return redirect("/captain/")

