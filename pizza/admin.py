from django.contrib import admin
from .models import User, Pizza, Salad, Cookie, IceCream, Beverage

# Register your models here.
admin.site.register(User)
admin.site.register(Pizza)
admin.site.register(Salad)
admin.site.register(Cookie)
admin.site.register(IceCream)
admin.site.register(Beverage)
