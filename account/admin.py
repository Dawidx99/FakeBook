from django.contrib import admin

# Register your models here.
from account.models import Account, Request

admin.site.register(Account)
admin.site.register(Request)