from django.contrib import admin
from api.models import User, TransactionCount

admin.site.register(User)


@admin.register(TransactionCount)
class TransactionCountAdmin(admin.ModelAdmin):
    list_display = ("user", "dailyCount", "monthlyCount", "yearlyCount", "modifiedDate")
