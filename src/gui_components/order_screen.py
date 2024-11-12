from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class OrderScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Place Order")
        
        layout = QVBoxLayout()
        
        self.info_label = QLabel("Select items to add to your order...")
        layout.addWidget(self.info_label)
        
        self.setLayout(layout)
