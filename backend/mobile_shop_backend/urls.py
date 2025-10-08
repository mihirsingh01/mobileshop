from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logins/', include('logins.urls')),
    path('super_admin/', include('super_admin.urls')),
    path('accessories_staff/', include('accessories_staff.urls')),
    path('repairing_staff/', include('repairing_staff.urls')),
    path('old_mobile_staff/', include('old_mobile_staff.urls')),
    path('promoter_staff/', include('promoter_staff.urls')),
    path('cashier/', include('cashier.urls')),
    path('sales/', include('sales.urls')),
    path('customer/', include('customer.urls')),
]
