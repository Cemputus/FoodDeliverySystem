from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login / Register")
        
        layout = QVBoxLayout()
        
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)
        
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)
        
        self.login_button = QPushButton("Login")
        layout.addWidget(self.login_button)
        
        self.register_button = QPushButton("Register")
        layout.addWidget(self.register_button)
        
        self.setLayout(layout)
