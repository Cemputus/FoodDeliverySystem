# # src/models/order.py
# import datetime
# from src.models.restaurant import MenuItem
# from src.utils import load_json, save_json

# class Order:
#     def __init__(self, user, restaurant, items):
#         self.user = user
#         self.restaurant = restaurant
#         self.items = items
#         self.status = "Pending"
#         self.placed_at = datetime.datetime.now()
#         self.save()

#     def calculate_total(self):
#         return sum(item.price for item in self.items)

#     def save(self):
#         orders = load_json('data/orders.json')
#         orders[f'{self.user.username}_{self.placed_at}'] = {
#             'restaurant': self.restaurant.name,
#             'items': [{'name': item.name, 'price': item.price} for item in self.items],
#             'status': self.status,
#             'placed_at': self.placed_at.isoformat()
#         }
#         save_json(orders, 'data/orders.json')

# class ScheduledOrder(Order):
#     def __init__(self, user, restaurant, items, scheduled_time):
#         super().__init__(user, restaurant, items)
#         self.scheduled_time = scheduled_time


# src/models/order.py
import json
from datetime import datetime

class Order:
    def __init__(self, order_id, user, items, scheduled=False):
        self.order_id = order_id
        self.user = user
        self.items = items
        self.scheduled = scheduled

    def place_order(self):
        # Logic to save the order to a file or database
        print("Order placed successfully.")

class ScheduledOrder(Order):  # Inheritance
    def __init__(self, order_id, user, items, scheduled_time):
        super().__init__(order_id, user, items, scheduled=True)
        self.scheduled_time = scheduled_time

    def place_order(self):  # Polymorphism
        # Overridden place_order method to handle scheduling
        if datetime.now() < self.scheduled_time:
            print("Order scheduled successfully.")
        else:
            super().place_order()
