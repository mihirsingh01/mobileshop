from django.urls import path
from . import views

urlpatterns = [
    path('punch/in/', views.punch_in_view, name='punch_in'),
    path('punch/out/', views.punch_out_view, name='punch_out'),
    path('product/add/', views.add_product_view, name='add_product'),
    path('product/list/', views.product_list_view, name='product_list'),
    path('sale/add/', views.add_sale_view, name='add_sale'),
    path('sale/list/', views.sales_list_view, name='sales_list'),
]
