from django.contrib import admin
from .models import Product, Color, Size, Subscriber, Message, Collection
# Register your models here.
admin.site.register(Product)
admin.site.register( Color)
admin.site.register(Size)
admin.site.register(Subscriber)
admin.site.register(Message)
admin.site.register(Collection)
