import sys
from tkinter import Widget
import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QFrame
from PyQt5.QtWidgets import QSizePolicy

class CameraDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Create a label to display the camera input
        self.image_label = QLabel(self)
        self.image_label.resize(800, 800)

        self.image_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

        # Start the camera input
        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            # Convert the frame to RGB format and display it on the label
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.image_label.setPixmap(pixmap)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a layout manager and add the label widget to it
        layout = QVBoxLayout()
        layout.minimumSize()
        # Add the CameraDialog to a QFrame so we can add a border
        dialog_frame = CameraDialog()
        layout.addWidget(dialog_frame)

        layout_h=QHBoxLayout()
        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')

        # Add the buttons to the layout
        button = QPushButton('Click me', self)
        button.resize(8,8)
        button.setStyleSheet('background-color: white')
        layout_h.addWidget(button)
        layout_h.addWidget(button1)
        layout_h.addWidget(button2)

        # Add the dialog frame to the main layout
        layout.addWidget(dialog_frame, stretch=1)
        layout.addLayout(layout_h)
        

        # Set the layout manager for the widget
        self.setLayout(layout)
        self.resize(800,800)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.setStyleSheet('background-color: black; border: 2px solid yellow;')
    widget.show()
    sys.exit(app.exec_())