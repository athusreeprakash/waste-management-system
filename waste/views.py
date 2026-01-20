from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.utils import timezone
from .models import *


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(username=uname, password=pwd)
        if user:
            auth_login(request, user)
            return redirect('/')
    return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


def user_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        password = request.POST.get('password')

        user = User.objects.create_user(username=email, password=password)
        UserType.objects.create(user=user, type='user')
        UserRegistration.objects.create(
            user=user,
            name=name,
            email=email,
            mobile=mobile,
            address=address,
            password=password,
            point=0,
            pincode=pincode
        )
        return redirect('/login/')
    return render(request, 'user_register.html')


def collector_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        password = request.POST.get('password')

        user = User.objects.create_user(username=email, password=password)
        UserType.objects.create(user=user, type='collector')
        CollectorRegistration.objects.create(
            collector_id=user,
            name=name,
            email=email,
            mobile=mobile,
            address=address,
            password=password
        )
        return redirect('/login/')
    return render(request, 'collector_register.html')


def request_pickup(request):
    user = UserRegistration.objects.get(user=request.user)
    if request.method == 'POST':
        WastePickup.objects.create(
            userid=user,
            status='requested',
            rdate=timezone.now()
        )
        return redirect('/pickup_status/')
    return render(request, 'request_pickup.html')


def pickup_status(request):
    user = UserRegistration.objects.get(user=request.user)
    pickups = WastePickup.objects.filter(userid=user)
    return render(request, 'pickup_status.html', {'pickups': pickups})


def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        point = request.POST.get('point')
        Category.objects.create(name=name, point=point)
        return redirect('/add_category/')
    return render(request, 'add_category.html')


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rate = request.POST.get('rate')
        point = request.POST.get('point')
        desc = request.POST.get('desc')
        image = request.FILES.get('image')
        Products.objects.create(
            name=name,
            rate=rate,
            point=point,
            desc=desc,
            image=image
        )
        return redirect('/add_product/')
    return render(request, 'add_product.html')


def complaints(request):
    user = UserRegistration.objects.get(user=request.user)
    if request.method == 'POST':
        subject = request.POST.get('subject')
        complaint = request.POST.get('complaint')
        Complaints.objects.create(
            user=user,
            subject=subject,
            complaint=complaint,
            rdate=timezone.now(),
            status='Pending'
        )
        return redirect('/complaints/')
    data = Complaints.objects.filter(user=user)
    return render(request, 'complaints.html', {'data': data})


def purchase(request):
    user = UserRegistration.objects.get(user=request.user)
    products = Products.objects.all()
    if request.method == 'POST':
        product_id = request.POST.get('product')
        qty = request.POST.get('quantity')
        product = Products.objects.get(id=product_id)
        total = int(product.rate) * int(qty)
        Purchase.objects.create(
            user=user,
            product=product,
            quantity=qty,
            mobile=user.mobile,
            address=user.address,
            pincode=user.pincode,
            type='ON',
            date=timezone.now(),
            status='Ordered',
            total=total
        )
        return redirect('/purchase/')
    return render(request, 'purchase.html', {'products': products})


def order_updates(request):
    user = UserRegistration.objects.get(user=request.user)
    orders = Purchase.objects.filter(user=user)
    return render(request, 'order_updates.html', {'orders': orders})
