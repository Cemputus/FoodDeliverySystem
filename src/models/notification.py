# src/models/notification.py
class Notification:
    def send_notification(self, message):
        print(f"Notification: {message}")

class OrderStatusNotification(Notification):
    def __init__(self, order):
        self.order = order

    def update_status(self, new_status):
        self.order.status = new_status
        self.send_notification(f"Order status updated to '{new_status}' for {self.order.user.username}")
