from django import forms
from .models import Category, Product, OldPhone, Repairing, Staff, CashCollection, Sale, Purchase

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'stock', 'price']

class OldPhoneForm(forms.ModelForm):
    class Meta:
        model = OldPhone
        fields = ['name', 'stock', 'price']

class RepairingForm(forms.ModelForm):
    class Meta:
        model = Repairing
        fields = ['product', 'description', 'status']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'attendance', 'payroll']

class CashCollectionForm(forms.ModelForm):
    class Meta:
        model = CashCollection
        fields = ['amount']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'quantity', 'total_price']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product', 'quantity', 'total_price']
