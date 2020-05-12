from django.contrib import admin
from .models import Members,MemberCoins,TotalCoins,CashIn,Staff,Checkin

admin.site.register(Members)
admin.site.register(MemberCoins)
admin.site.register(TotalCoins)
admin.site.register(CashIn)
admin.site.register(Staff)
admin.site.register(Checkin)
# Register your models here.
