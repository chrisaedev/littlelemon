from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Menu, Table

class MenuAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item = Menu.objects.create(name="Test Menu Item", description="Test Description", price=10.99)

    def test_get_menu_items(self):
        response = self.client.get('/menus/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_menu_item(self):
        data = {
            "name": "New Menu Item",
            "description": "New Description",
            "price": 15.99
        }
        response = self.client.post('/menus/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 2)

class TableAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.table_booking = Table.objects.create(table_number=1, booking_date_time="2024-03-06T10:00:00Z", customer_name="Test Customer", customer_phone="1234567890")

    def test_get_table_bookings(self):
        response = self.client.get('/tables/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_table_booking(self):
        data = {
            "table_number": 2,
            "booking_date_time": "2024-03-06T12:00:00Z",
            "customer_name": "New Customer",
            "customer_phone": "9876543210"
        }
        response = self.client.post('/tables/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Table.objects.count(), 2)
