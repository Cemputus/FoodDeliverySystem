from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class RestaurantScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Browse Restaurants")
        
        layout = QVBoxLayout()
        
        self.info_label = QLabel("Browse available restaurants here...")
        layout.addWidget(self.info_label)
        
        self.setLayout(layout)
