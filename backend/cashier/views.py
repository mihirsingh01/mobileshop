from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SaleCollection
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@login_required
def sales_collection_list(request):
    collections = SaleCollection.objects.all()
    return render(request, 'cashier/sales_collection_list.html', {'collections': collections})

@login_required
def add_sales_collection(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        mrp = request.POST.get('mrp')
        sale_price = request.POST.get('sale_price')
        payment_type = request.POST.get('payment_type')
        payment_status = request.POST.get('payment_status')
        sales_person = request.user
        SaleCollection.objects.create(
            product_name=product_name,
            mrp=mrp,
            sale_price=sale_price,
            payment_type=payment_type,
            payment_status=payment_status,
            sales_person=sales_person
        )
        return redirect('sales_collection_list')
    return render(request, 'cashier/add_sales_collection.html')
