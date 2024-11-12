from src.gui_components.main_window import MainWindow
from PyQt5.QtWidgets import QApplication

# Application entry point
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
