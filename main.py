# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QLineEdit
from PyQt5.QtGui import QFont


# Main App Objects and Settings


class Calci(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.resize(300, 400)

        # Create all App Widgets and Objects

        self.display = QLineEdit()
        self.display.setFont(QFont("helvetica",32))

        self.c_button = QPushButton('C')
        self.g_button = QPushButton('<')
        # Grid Layout Special case
        row = 0
        col = 0

        self.list_button = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']
        self.row2 = QGridLayout()
        for text in self.list_button:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            button.setStyleSheet("QPushButton {font : 25pt ComicSans MS; padding : 10px;}")
            self.row2.addWidget(button, row, col)
            col = col + 1

            if col > 3:
                row = row + 1
                col = 0

        # All Design Here - LAYOUTS
        self.master_layout = QVBoxLayout()

        self.row1 = QHBoxLayout()

        self.row3 = QHBoxLayout()

        self.row1.addWidget(self.display)

        self.row3.addWidget(self.c_button)
        self.row3.addWidget(self.g_button)

        # Master Layout Add
        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2)
        self.master_layout.addLayout(self.row3)
        self.master_layout.setContentsMargins(25,25,25,25)

        self.setLayout(self.master_layout)
        # Create Functions
        self.c_button.clicked.connect(self.button_click)
        self.c_button.setStyleSheet("QPushButton {font : 25pt ComicSans MS; padding : 10px;}")
        self.g_button.clicked.connect(self.button_click)
        self.g_button.setStyleSheet("QPushButton {font : 25pt ComicSans MS; padding : 10px;}")
    # Create Functions

    def button_click(self):
        button = app.sender()
        text = button.text()

        if text == "=":
            display_text = self.display.text()
            try:
                expression = eval(display_text)
                self.display.setText(str(expression))
            except Exception as e:
                print("Error:", e)

        elif text == "C":
            self.display.clear()

        elif text == "<":
            current_value = self.display.text()
            new_value = current_value[:-1]
            self.display.setText(new_value)

        else:
            current_value = self.display.text()
            self.display.setText(current_value + text)


# Events

# Show/Run our App
if __name__ == "__main__":
    app = QApplication([])
    main_window = Calci()
    main_window.setStyleSheet("QWidget {background-color: #f0f0f8")
    main_window.show()
    app.exec_()
