from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('sales/list/', views.sales_list_view, name='sales_list'),
    path('sales/add/', views.sales_add_view, name='sales_add'),
    path('repairing/list/', views.repairing_list_view, name='repairing_list'),
    path('repairing/add/', views.repairing_add_view, name='repairing_add'),
    path('staff/attendance/', views.staff_attendance_view, name='staff_attendance'),
    path('staff/payroll/', views.staff_payroll_view, name='staff_payroll'),
    path('staff/add/', views.staff_add_view, name='staff_add'),
    path('cash/collect/', views.cash_collect_view, name='cash_collect'),
    path('report/sales/', views.report_sales_view, name='report_sales'),
    path('report/purchase/', views.report_purchase_view, name='report_purchase'),
]
