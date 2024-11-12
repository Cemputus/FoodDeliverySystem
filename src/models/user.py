# # src/models/user.py
# import hashlib
# from src.utils import load_json, save_json

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password_hash = self._hash_password(password)
#         self.order_history = []

#     def _hash_password(self, password):
#         return hashlib.sha256(password.encode()).hexdigest()

#     def check_password(self, password):
#         return self.password_hash == self._hash_password(password)

#     def add_order_to_history(self, order):
#         self.order_history.append(order)
#         self.save()

#     def save(self):
#         users = load_json('data/users.json')
#         users[self.username] = {
#             'password_hash': self.password_hash,
#             'order_history': self.order_history
#         }
#         save_json(users, 'data/users.json')

#     @staticmethod
#     def load(username):
#         users = load_json('data/users.json')
#         if username in users:
#             data = users[username]
#             user = User(username, "")
#             user.password_hash = data['password_hash']
#             user.order_history = data['order_history']
#             return user
#         return None



# src/models/user.py
import json
import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self._password = self._encrypt_password(password)  # Encapsulation

    def _encrypt_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def authenticate(self, password):
        return self._password == self._encrypt_password(password)

    def save_to_file(self):
        with open('data/users.json', 'a') as f:
            f.write(json.dumps({"username": self.username, "password": self._password}) + "\n")
