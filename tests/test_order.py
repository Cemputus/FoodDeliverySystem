# tests/test_order.py
import unittest
from src.models.order import Order, ScheduledOrder
from src.models.user import User
from src.models.restaurant import Restaurant, MenuItem

class TestOrder(unittest.TestCase):
    def test_order_total(self):
        user = User("test_user", "test_password")
        restaurant = Restaurant("Test Restaurant")
        items = [MenuItem("Burger", 10), MenuItem("Fries", 5)]
        order = Order(user, restaurant, items)
        self.assertEqual(order.calculate_total(), 15)

    def test_scheduled_order(self):
        user = User("test_user", "test_password")
        restaurant = Restaurant("Test Restaurant")
        items = [MenuItem("Burger", 10)]
        scheduled_time = "2024-12-12 15:00"
        order = ScheduledOrder(user, restaurant, items, scheduled_time)
        self.assertEqual(order.scheduled_time, scheduled_time)

if __name__ == '__main__':
    unittest.main()
