# # src/gui_components/main_window.py
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
# from login_screen import LoginScreen
# from restaurant_screen import RestaurantScreen
# from order_screen import OrderScreen
# from feedback_screen import FeedbackScreen

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Food Delivery System")

#         # Set up the layout
#         central_widget = QWidget()
#         layout = QVBoxLayout()

#         # Create buttons to navigate to different screens
#         self.login_button = QPushButton("Login / Register")
#         self.login_button.clicked.connect(self.open_login_screen)
#         layout.addWidget(self.login_button)

#         self.browse_button = QPushButton("Browse Restaurants")
#         self.browse_button.clicked.connect(self.open_restaurant_screen)
#         layout.addWidget(self.browse_button)

#         self.order_button = QPushButton("Place Order")
#         self.order_button.clicked.connect(self.open_order_screen)
#         layout.addWidget(self.order_button)

#         self.feedback_button = QPushButton("Submit Feedback")
#         self.feedback_button.clicked.connect(self.open_feedback_screen)
#         layout.addWidget(self.feedback_button)

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#     def open_login_screen(self):
#         self.login_screen = LoginScreen()
#         self.login_screen.show()

#     def open_restaurant_screen(self):
#         self.restaurant_screen = RestaurantScreen()
#         self.restaurant_screen.show()

#     def open_order_screen(self):
#         self.order_screen = OrderScreen()
#         self.order_screen.show()

#     def open_feedback_screen(self):
#         self.feedback_screen = FeedbackScreen()
#         self.feedback_screen.show()



from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton
from .login_screen import LoginScreen
from .restaurant_screen import RestaurantScreen
from .order_screen import OrderScreen
from .feedback_screen import FeedbackScreen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Food Delivery System")

        central_widget = QWidget()
        layout = QVBoxLayout()

        self.login_button = QPushButton("Login / Register")
        self.login_button.clicked.connect(self.open_login_screen)
        layout.addWidget(self.login_button)

        self.browse_button = QPushButton("Browse Restaurants")
        self.browse_button.clicked.connect(self.open_restaurant_screen)
        layout.addWidget(self.browse_button)

        self.order_button = QPushButton("Place Order")
        self.order_button.clicked.connect(self.open_order_screen)
        layout.addWidget(self.order_button)

        self.feedback_button = QPushButton("Submit Feedback")
        self.feedback_button.clicked.connect(self.open_feedback_screen)
        layout.addWidget(self.feedback_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_login_screen(self):
        self.login_screen = LoginScreen()
        self.login_screen.show()

    def open_restaurant_screen(self):
        self.restaurant_screen = RestaurantScreen()
        self.restaurant_screen.show()

    def open_order_screen(self):
        self.order_screen = OrderScreen()
        self.order_screen.show()

    def open_feedback_screen(self):
        self.feedback_screen = FeedbackScreen()
        self.feedback_screen.show()
