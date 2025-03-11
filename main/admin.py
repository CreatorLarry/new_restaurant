from django.contrib import admin

from main.models import Dish, Reservation, Order

# Register your models here.
admin.site.register(Dish)
admin.site.register(Reservation)
admin.site.register(Order)