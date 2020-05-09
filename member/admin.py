from django.contrib import admin
from .models import Members,MemberCoins,TotalCoins,CashIn

admin.site.register(Members)
admin.site.register(MemberCoins)
admin.site.register(TotalCoins)
admin.site.register(CashIn)
# Register your models here.
