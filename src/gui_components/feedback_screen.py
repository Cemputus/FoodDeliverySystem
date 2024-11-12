from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton

class FeedbackScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Feedback")
        
        layout = QVBoxLayout()
        
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Your Name")
        layout.addWidget(self.name_input)
        
        self.feedback_input = QTextEdit(self)
        self.feedback_input.setPlaceholderText("Enter your feedback here...")
        layout.addWidget(self.feedback_input)
        
        self.submit_button = QPushButton("Submit Feedback")
        layout.addWidget(self.submit_button)
        
        self.setLayout(layout)
