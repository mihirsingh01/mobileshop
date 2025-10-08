from django import forms

class LoginForm(forms.Form):
    LOGIN_TYPE_CHOICES = [
        ('super', 'Super'),
        ('cashier', 'Cashier'),
        ('staff', 'Staff'),
        ('customer', 'Customer'),
        ('manager', 'Manager'),
    ]
    login_type = forms.ChoiceField(choices=LOGIN_TYPE_CHOICES, label="Login Type")
    username = forms.CharField(max_length=150, label="User Name")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
