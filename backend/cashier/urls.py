from django.urls import path
from . import views

urlpatterns = [
    path('sales/collection/list/', views.sales_collection_list, name='sales_collection_list'),
    path('sales/collection/add/', views.add_sales_collection, name='add_sales_collection'),
]
