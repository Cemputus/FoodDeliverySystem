# tests/test_user.py
import unittest
from src.models.user import User

class TestUser(unittest.TestCase):
    def test_password_hashing(self):
        user = User("test_user", "test_password")
        self.assertTrue(user.check_password("test_password"))
        self.assertFalse(user.check_password("wrong_password"))

    def test_order_history(self):
        user = User("test_user", "test_password")
        user.add_order_to_history("Test Order")
        self.assertIn("Test Order", user.order_history)

if __name__ == '__main__':
    unittest.main()
