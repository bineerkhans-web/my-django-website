from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from . models import *

def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        print(name,password)
        user=User_registration.objects.filter(name=name,password=password)
        if user:
            return redirect('home')
        return redirect('login_view')
    else:
        return render(request, 'login.html')

def login(request):
    return login_view(request)

def index(request):
    foods= Dish.objects.all()
    context={
        'foods':foods
    }
    print(foods)
    return render(request, 'index.html',context)

def menu(request):
    foods= Dish.objects.all()
    context={
        'foods':foods
    }
    print(foods)
    return render(request, 'menu.html',context)

def about(request):
    return render(request, 'about.html')

def book(request):
    return render(request, 'book.html')

def cart(request):
    return render(request,'cart.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        print(name,phone,password)
        User_registration.objects.create(name=name,phone=phone,password=password)
        return redirect('login_view')
    else:
        return render(request, 'register.html')
    
def additems(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        print(name, description, image)
        if name:
            Dish.objects.create(name=name, description=description or '', image=image)
            messages.success(request, 'Dish added successfully!')
            return redirect('menu')
        else:
            messages.error(request, 'Menu name is required.')
    return render(request, 'additems.html')

def viewitem(request):
    items = Dish.objects.all()
    context = {
        'items': items
    }
    return render(request, 'viewitem.html', context)

def update_item(request, item_id):
    try:
        item = Dish.objects.get(id=item_id)
    except Dish.DoesNotExist:
        messages.error(request, 'Item not found.')
        return redirect('viewitem')
    
    if request.method == 'POST':
        item_name = request.POST.get('name')
        item_description = request.POST.get('description')
        item_image = request.FILES.get('image')
        print(item_name, item_description, item_image)
        
        if item_name:
            item.name = item_name
        if item_description:
            item.description = item_description
        if item_image:
            item.image = item_image
        item.save()
        messages.success(request, 'Item updated successfully!')
        return redirect('viewitem')
    
    context = {
        'item': item
    }
    return render(request, 'update_item.html', context)
    
def delete_item(request, item_id):
    try:
        item = Dish.objects.get(id=item_id)
        item.delete()
        messages.success(request, 'Item deleted successfully!')
    except Dish.DoesNotExist:
        messages.error(request, 'Item not found.')
    return redirect('viewitem')
