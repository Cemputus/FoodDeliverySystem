# # src/models/payment.py
# class PaymentProcessor:
#     def process_payment(self, amount):
#         raise NotImplementedError("This method should be overridden by subclasses.")

# class CreditCardPayment(PaymentProcessor):
#     def __init__(self, card_number, expiry_date, cvv):
#         self.card_number = card_number
#         self.expiry_date = expiry_date
#         self.cvv = cvv

#     def process_payment(self, amount):
#         print(f"Processing credit card payment of ${amount}")
#         # Implement card validation and transaction here
#         return True

# class DigitalWalletPayment(PaymentProcessor):
#     def __init__(self, wallet_id):
#         self.wallet_id = wallet_id

#     def process_payment(self, amount):
#         print(f"Processing digital wallet payment of ${amount}")
#         # Implement wallet transaction here
#         return True




# src/models/payment.py

class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclass must implement process_payment method")

class CreditCardPayment(PaymentProcessor):  # Polymorphism
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class DigitalWalletPayment(PaymentProcessor):  # Polymorphism
    def process_payment(self, amount):
        print(f"Processing digital wallet payment of {amount}")

