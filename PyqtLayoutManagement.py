import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel
#version 5.15.11
class LayoutDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt Layout Demo')
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # Vertical Layout
        vbox = QVBoxLayout()
        vbox.addWidget(QPushButton('Button 1'))
        vbox.addWidget(QPushButton('Button 2'))
        vbox.addWidget(QPushButton('Button 3'))

        # Horizontal Layout
        hbox = QHBoxLayout()
        hbox.addWidget(QPushButton('Left'))
        hbox.addWidget(QPushButton('Center'))
        hbox.addWidget(QPushButton('Right'))

        # Grid Layout
        grid = QGridLayout()
        grid.addWidget(QPushButton('1'), 0, 0)
        grid.addWidget(QPushButton('2'), 0, 1)
        grid.addWidget(QPushButton('3'), 0, 2)
        grid.addWidget(QPushButton('4'), 1, 0)
        grid.addWidget(QPushButton('5'), 1, 1)
        grid.addWidget(QPushButton('6'), 1, 2)

        main_layout.addWidget(QLabel('Vertical Layout:'))
        main_layout.addLayout(vbox)
        main_layout.addWidget(QLabel('Horizontal Layout:'))
        main_layout.addLayout(hbox)
        main_layout.addWidget(QLabel('Grid Layout:'))
        main_layout.addLayout(grid)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = LayoutDemo()
    demo.show()
    sys.exit(app.exec_())

"""
This script demonstrates different layout management techniques in PyQt:
1. QVBoxLayout for vertical arrangement of widgets
2. QHBoxLayout for horizontal arrangement of widgets
3. QGridLayout for grid-based arrangement of widgets
4. Nesting layouts for complex UI designs

Key points:
- Layouts automatically handle widget sizing and positioning
- Layouts can be nested to create complex UI structures
- QMainWindow provides a framework for building application windows

Applications:
1. Creating responsive and flexible GUIs
2. Building complex application layouts
3. Designing forms and data entry interfaces
"""