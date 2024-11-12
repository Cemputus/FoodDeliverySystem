# src/gui.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Food Delivery System")

        # Central Widget
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Add Buttons
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.show_login)
        layout.addWidget(self.login_button)

        self.browse_button = QPushButton("Browse Restaurants")
        self.browse_button.clicked.connect(self.browse_restaurants)
        layout.addWidget(self.browse_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_login(self):
        QMessageBox.information(self, "Login", "This would open the login screen.")

    def browse_restaurants(self):
        QMessageBox.information(self, "Browse", "This would open the restaurant browsing screen.")

# Run the Application
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
