from django.shortcuts import render,redirect
from .models import Members,MemberCoins, TotalCoins, CashIn
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


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
        inventory=TotalCoins.objects.all()[0]
        return render(request,'coins.html',{"members":members,"inventory":inventory})




