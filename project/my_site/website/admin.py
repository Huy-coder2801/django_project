from django.contrib import admin
from .models import Customer, Category, Order, Driver
# Register your models here.
admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Category)
admin.site.register(Order)