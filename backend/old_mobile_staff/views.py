from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Attendance, Product, Sale
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@login_required
def punch_in_view(request):
    attendance, created = Attendance.objects.get_or_create(user=request.user)
    attendance.punch_in = timezone.now()
    attendance.save()
    return HttpResponse("Punched In at " + str(attendance.punch_in))

@login_required
def punch_out_view(request):
    attendance, created = Attendance.objects.get_or_create(user=request.user)
    attendance.punch_out = timezone.now()
    attendance.save()
    return HttpResponse("Punched Out at " + str(attendance.punch_out))

@login_required
def add_product_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        if name and quantity:
            Product.objects.create(name=name, quantity=int(quantity))
            return redirect('product_list')
    return render(request, 'old_mobile_staff/add_product.html')

@login_required
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'old_mobile_staff/product_list.html', {'products': products})

@login_required
def add_sale_view(request):
    if request.method == 'POST':
        product_id = request.POST.get('product')
        mrp = request.POST.get('mrp')
        sale_price = request.POST.get('sale_price')
        payment_type = request.POST.get('payment_type')
        payment_status = request.POST.get('payment_status')
        sales_person = request.user
        product = Product.objects.get(id=product_id)
        Sale.objects.create(
            product=product,
            mrp=mrp,
            sale_price=sale_price,
            payment_type=payment_type,
            payment_status=payment_status,
            sales_person=sales_person
        )
        return redirect('sales_list')
    products = Product.objects.all()
    return render(request, 'old_mobile_staff/add_sale.html', {'products': products})

@login_required
def sales_list_view(request):
    sales = Sale.objects.all()
    return render(request, 'old_mobile_staff/sales_list.html', {'sales': sales})

@api_view(['GET'])
def api_list(request):
    products = Product.objects.all().values()
    return Response(list(products))
