from django.contrib import admin
from .models import BanksList
# Register your models here.

@admin.register(BanksList)
class BanksListAdmin(admin.ModelAdmin):
    list_display = ['branch', 'bank_name', 'state']