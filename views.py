from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponse
from .forms import *
from .models import *
import datetime

# Create your views here.

def hire_toonie(request):
    template_name='hireToonie.html'
    form = OrderForm()
    context = {'form':form}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order_form = form.save(commit=False)
            order_form.client = request.user 
            print(request.user)
            order_form.save()
            notif_body = f'{request.user} from {form.cleaned_data.get("address")} posted a new job on'
            notification = Notification(owner=request.user, order=order_form, body=notif_body, timestamp=datetime.datetime.now)
            notification.save()
            return redirect('success')
    return render (request, template_name, context)


def hire_driver(request):
    template_name = 'hireDriver.html'
    form = OrderForm()
    context = {'form':form}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            hire_form = form.save(commit=False)
            hire_form.client = request.user 
            hire_form.save()
            return redirect('success')
    return render(request, template_name, context)


def success(request):
    template_name = 'success.html'
    return render(request, template_name)


def chat(request):
    template_name = 'chat.html'
    return render(request, template_name)


def notify(request):
    template_name = 'notification.html'
    notifications = Notification.objects.filter(viewed=False)
    context = {'notifications':notifications}
    return render(request, template_name, context)


def notification_detail(request, pk):
    notification = Notification.objects.get(id=pk)
    template_name = 'notifdet.html'
    context = {'notification':notification}
    return render(request, template_name, context)


def accept(request):
    template_name='toonsuccess.html'
    if request.method == 'POST':
        notif_id = request.POST.get('notif_id')
        notification = Notification.objects.get(id=notif_id)
        notification.viewed = True
        notification.save()
        body = f'{request.user} has accepted your offer'
        message = Message(notification_order=notification.order, notification=notification, sender=request.user, body=body, timestamp=datetime.datetime.now)
        message.save()
    return render(request, template_name)



def my_orders(request, pk):
    orders = Order.objects.filter(client_id=pk)
    context = {'orders':orders}
    template_name = 'my_orders.html'
    return render(request, template_name, context)


def order_detail(request, pk):
    template_name = 'order_detail.html'
    order = Order.objects.get(id=pk)
    messages = Message.objects.filter(notification_order_id=pk)
    context = {'order':order,'messages':messages}
    return render(request, template_name, context)


def ToonieContact(request, pk):
    template_name = 'ToonieContact.html'
    message = Message.objects.get(id=pk)
    context = {'message':message}
    return render(request, template_name, context)


def reject(request):
    template_name = 'ToonieContact.html'
    if request.method == 'POST':
        message_id = request.POST.get('message_id')
        message = Message.objects.get(id=message_id)
        notif = message.notification
        body = f'{message.notification_order.client.username} has turned down your offer'
        print(f' this is the notification{notif.body}')
        if notif.viewed==True:
            notif.viewed = False
            notif.save()
        toonie_message = ClientMessage(message=message, body=body, timestamp=datetime.datetime.now)
        toonie_message.save()
    return redirect('emotional-damage')


def hire(request):
    template_name = 'hiresuccess.html'
    if request.method == 'POST':
        message_id = request.POST.get('message_id')
        message = Message.objects.get(id=message_id)
        body = f'{message.notification_order.client.username} has accepted your offer'
        #the message to the toonie from the client
        toonie_message = ClientMessage(message=message, body=body, timestamp=datetime.datetime.now)
        toonie_message.save()
    return render(request, template_name)


def my_messages(request, pk):
    template_name = 'messages.html'
    messages = Message.objects.filter(sender_id=pk)
    context = {'messages': messages}
    return render(request, template_name, context)


def message_detail(request, pk):
    message_info = Message.objects.get(id=pk)
    toonie_messages = ClientMessage.objects.filter(message_id=pk)
    context = {'message_info': message_info, 'toonie_messages':toonie_messages}
    template_name = 'message_detail.html'
    return render(request, template_name, context)


def denied(request):
    template_name = 'online.html'
    return render(request, template_name)


def ClientContact(request, pk):
    toonie_message = ClientMessage.objects.get(id=pk)
    context = {'toonie_message':toonie_message}
    template_name = 'ClientContact.html'
    return render(request, template_name, context)


