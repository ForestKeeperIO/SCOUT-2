from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QGridLayout, QHBoxLayout
from PySide6.QtCore import Qt

class PhoneFrame(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.number_display = QLabel("")
        self.number_display.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.number_display, 1)

        dialpad_layout = QGridLayout()
        layout.addLayout(dialpad_layout, 2)
        for i, digit in enumerate("123456789*0#"):
            button = QPushButton(digit)
            button.clicked.connect(lambda _, digit=digit: self.update_number_display(digit))
            button.setStyleSheet("""
                QPushButton {
                    background-color: #2d2d2d; 
                    color: #ffffff;
                    border-radius: 50%; 
                    padding: 10px; 
                }
            """)
            dialpad_layout.addWidget(button, i // 3, i % 3)

        # Call Control Buttons
        call_controls_layout = QHBoxLayout()
        layout.addLayout(call_controls_layout) 

        self.call_button = QPushButton("Call")
        self.call_button.setCheckable(True)
        self.call_button.setStyleSheet("""
            QPushButton {
                background-color: #2d2d2d; 
                color: #ffffff;
                border-radius: 15px; 
                padding: 10px; 
            }
        """)
        call_controls_layout.addWidget(self.call_button)

        for label in ["Mute", "Hold"]:
            button = QPushButton(label)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #2d2d2d; 
                    color: #ffffff;
                    border-radius: 15px; 
                    padding: 10px; 
                }
            """)
            call_controls_layout.addWidget(button)

    def update_number_display(self, digit):
        current_text = self.number_display.text()
        self.number_display.setText(current_text + digit)