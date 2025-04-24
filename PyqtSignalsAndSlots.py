import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal, QObject

class Communicator(QObject):
    signal = pyqtSignal(str)

class SignalSlotDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt Signals and Slots Demo')
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.line_edit = QLineEdit()
        self.button = QPushButton('Send Message')
        self.label = QLabel('Message will appear here')

        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.button.clicked.connect(self.on_button_clicked)

        self.communicator = Communicator()
        self.communicator.signal.connect(self.update_label)

    def on_button_clicked(self):
        text = self.line_edit.text()
        self.communicator.signal.emit(text)

    def update_label(self, message):
        self.label.setText(f"Received: {message}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = SignalSlotDemo()
    demo.show()
    sys.exit(app.exec_())

"""
This script demonstrates the use of signals and slots in PyQt:
1. Creating custom signals
2. Connecting signals to slots
3. Emitting signals and passing data

Key points:
- Signals and slots provide a type-safe way for objects to communicate
- Custom signals can be created using pyqtSignal
- The connect() method is used to connect signals to slots
- emit() is used to send a signal

Applications:
1. Handling user interactions (button clicks, text input)
2. Implementing custom event systems
3. Creating loosely coupled communication between objects
4. Building reactive user interfaces
"""