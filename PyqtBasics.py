import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
#5.15.11
class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Basic Example')
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        self.label = QLabel('Welcome to PyQt5!', self)
        layout.addWidget(self.label)

        button = QPushButton('Click Me', self)
        button.clicked.connect(self.on_click)
        layout.addWidget(button)

        self.setLayout(layout)

    def on_click(self):
        self.label.setText('Button clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec_())

"""
This script introduces basic PyQt5 concepts:
1. Creating a QApplication instance
2. Defining a custom window class
3. Setting up a layout (QVBoxLayout)
4. Adding widgets (QLabel, QPushButton)
5. Connecting signals and slots (button click event)
6. Running the application event loop

To run: 
1. Install PyQt5: pip install PyQt5
2. Execute this script with Python

Applications:
1. Developing cross-platform desktop applications
2. Creating complex user interfaces
3. Building data visualization tools
4. Developing scientific or engineering applications
"""