from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def dashboard_view(request):
    return render(request, 'super_admin/dashboard.html')

@login_required
def sales_list_view(request):
    sales = Sale.objects.all()
    return render(request, 'super_admin/sales_list.html', {'sales': sales})

@login_required
def sales_add_view(request):
    if request.method == 'POST':
        # Implement adding sales logic here
        pass
    return render(request, 'super_admin/sales_add.html')

@login_required
def repairing_list_view(request):
    repairings = Repairing.objects.all()
    return render(request, 'super_admin/repairing_list.html', {'repairings': repairings})

@login_required
def repairing_add_view(request):
    if request.method == 'POST':
        # Implement adding repairing logic here
        pass
    return render(request, 'super_admin/repairing_add.html')

@login_required
def staff_attendance_view(request):
    staffs = Staff.objects.all()
    return render(request, 'super_admin/staff_attendance.html', {'staffs': staffs})

@login_required
def staff_payroll_view(request):
    staffs = Staff.objects.all()
    return render(request, 'super_admin/staff_payroll.html', {'staffs': staffs})

@login_required
def staff_add_view(request):
    if request.method == 'POST':
        # Implement adding staff logic here
        pass
    return render(request, 'super_admin/staff_add.html')

@login_required
def cash_collect_view(request):
    if request.method == 'POST':
        # Implement cash collection logic here
        pass
    return render(request, 'super_admin/cash_collect.html')

@login_required
def report_sales_view(request):
    # Implement sales report logic here
    return render(request, 'super_admin/report_sales.html')

@login_required
def report_purchase_view(request):
    # Implement purchase report logic here
    return render(request, 'super_admin/report_purchase.html')
