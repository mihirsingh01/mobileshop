from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Attendance, Product, Sale

class AccessoriesStaffTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_punch_in(self):
        response = self.client.get(reverse('punch_in'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Punched In', response.content.decode())

    def test_punch_out(self):
        response = self.client.get(reverse('punch_out'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Punched Out', response.content.decode())

    def test_add_product(self):
        response = self.client.post(reverse('add_product'), {'name': 'Test Product', 'quantity': 10})
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Product.objects.filter(name='Test Product').exists())

    def test_product_list(self):
        Product.objects.create(name='Test Product', quantity=10)
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')

    def test_add_sale(self):
        product = Product.objects.create(name='Test Product', quantity=10)
        response = self.client.post(reverse('add_sale'), {
            'product': product.pk,
            'mrp': '100.00',
            'sale_price': '80.00',
            'payment_type': 'cash',
            'payment_status': 'paid',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Sale.objects.filter(product=product).exists())

    def test_sales_list(self):
        product = Product.objects.create(name='Test Product', quantity=10)
        Sale.objects.create(product=product, mrp=100, sale_price=80, payment_type='cash', payment_status='paid', sales_person=self.user)
        response = self.client.get(reverse('sales_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')
