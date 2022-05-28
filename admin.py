from django.contrib import admin
from .models import Order, Notification, Message, ClientMessage

# Register your models here.
admin.site.register(Order)
admin.site.register(Notification)
admin.site.register(Message)
admin.site.register(ClientMessage)