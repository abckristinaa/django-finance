from django.contrib import admin

from .models import Account, AccountOperation, Operation

admin.site.register([Account, AccountOperation, Operation])
