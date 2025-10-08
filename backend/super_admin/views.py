from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("Super Admin Dashboard")

def sales_list(request):
    return HttpResponse("Sales List")

def sales_add(request):
    return HttpResponse("Add Sale")

def repairing_list(request):
    return HttpResponse("Repairing List with filter options")

def repairing_add(request):
    return HttpResponse("Add Repairing")

def staff_attendance(request):
    return HttpResponse("Staff Attendance")

def staff_payroll(request):
    return HttpResponse("Staff Payroll")

def staff_add(request):
    return HttpResponse("Add Staff")

def cash_collect(request):
    return HttpResponse("Collect All Cash")

def report_sales(request):
    return HttpResponse("Sales Report")

def report_purchase(request):
    return HttpResponse("Purchase Report")
