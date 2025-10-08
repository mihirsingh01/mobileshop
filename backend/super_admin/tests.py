from django.test import TestCase
from super_admin.models import Category, Product, OldPhone, Repairing, Staff, CashCollection, Sale, Purchase

class SuperAdminModelTests(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(name='Test Category')
        self.assertEqual(str(category), 'Test Category')

    def test_product_creation(self):
        category = Category.objects.create(name='Test Category')
        product = Product.objects.create(category=category, name='Test Product', stock=10, price=99.99)
        self.assertEqual(str(product), 'Test Product')

    def test_oldphone_creation(self):
        old_phone = OldPhone.objects.create(name='Old Phone', stock=5, price=49.99)
        self.assertEqual(str(old_phone), 'Old Phone')

    def test_repairing_creation(self):
        category = Category.objects.create(name='Test Category')
        product = Product.objects.create(category=category, name='Test Product', stock=10, price=99.99)
        repairing = Repairing.objects.create(product=product, description='Fix screen', status='Pending')
        self.assertIn('Repairing', str(repairing))

    def test_staff_creation(self):
        staff = Staff.objects.create(name='John Doe', attendance=20, payroll=1500.00)
        self.assertEqual(str(staff), 'John Doe')

    def test_cashcollection_creation(self):
        cash = CashCollection.objects.create(amount=1000.00)
        self.assertEqual(cash.amount, 1000.00)

    def test_sale_creation(self):
        category = Category.objects.create(name='Test Category')
        product = Product.objects.create(category=category, name='Test Product', stock=10, price=99.99)
        sale = Sale.objects.create(product=product, quantity=2, total_price=199.98)
        self.assertEqual(sale.quantity, 2)

    def test_purchase_creation(self):
        category = Category.objects.create(name='Test Category')
        product = Product.objects.create(category=category, name='Test Product', stock=10, price=99.99)
        purchase = Purchase.objects.create(product=product, quantity=5, total_price=499.95)
        self.assertEqual(purchase.quantity, 5)
