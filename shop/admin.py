from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Outlet)
admin.site.register(Order)
admin.site.register(Tag)
