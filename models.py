from django.db import models
from django.conf import settings

# Create your models here.
PLACES = (
    ('Thika', 'Thika'),
    ('Makongeni', 'Makongeni'),
    ('Runda', 'Runda'),
    ('Kiganjo', 'Kiganjo'),
    ('Section 9', 'Section 9'),
    ('Starehe', 'Starehe'),
    ('Mkere', 'Mkere')
)


class Order(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    description = models.TextField(null=True)
    address = models.CharField(max_length=100, choices=PLACES)


class Notification(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='owner')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    viewed = models.BooleanField(default=False)


class Message(models.Model):
    notification_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)


class ClientMessage(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    
