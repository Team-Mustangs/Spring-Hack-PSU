import sys
from tkinter import Widget, dialog
from turtle import color
import cv2
from PyQt5.QtCore import Qt, QTimer, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QFrame, QLineEdit
from PyQt5.QtWidgets import QSizePolicy
import threading

#footer - collaboration
'''
1) Color scheme
2) 
'''

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
        self.start_webcam()

    def update_frame(self):
        ret, frame = self.capture.read()

        frame = cv2.flip(frame, 1)

        if ret:
            # Convert the frame to RGB format and display it on the label
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.image_label.setPixmap(pixmap)

    def update_label(self):
        new_label=QLabel(self)
        new_label.setStyleSheet('background-color: #000000')
        pixmap=QPixmap('C:/Users/harsh/OneDrive/Documents/GitHub/Spring-Hack-PSU/image.png')
        pixmap = pixmap.scaled(640, 480, Qt.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)

    def start_webcam(self):
        self.image_label.clear()
        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def stop_webcam(self):
        self.timer.stop()
        if self.capture:
            self.capture.release()
        self.update_label()

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.switch=True
        self.dialog_frame = CameraDialog()

        self.text_label = QLabel("<h1>Translation</h1>", self) 
        font = QFont('Arial', 12)

        self.text_label.setFont(font)
        self.text_label.setStyleSheet('background-color: #ffffff ; border: 2px solid black ; border-radius: 10px; color: #D22E1E')
        self.text_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        button1 = QPushButton('On/Off', self)

        button1.setMinimumHeight(50)
        button1.setStyleSheet('background-color: #ffffff; border-radius: 10px')
        button1.clicked.connect(self.on_click1)
        button1.setFont(font)

        button2 = QPushButton('Translate', self)

        button2.setMinimumHeight(50)
        button2.setStyleSheet('background-color: #ffffff; border-radius: 10px')
        button2.clicked.connect(self.on_click2)
        button2.setFont(font)

        #button layout
        layout_b = QHBoxLayout()

        layout_b.addWidget(button1)
        layout_b.addWidget(button2)

        layout1 = QVBoxLayout()
        layout1.addWidget(self.dialog_frame)
        layout1.addLayout(layout_b)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.text_label)

        layout2.insertLayout(0, layout1)

        self.setLayout(layout2)
        self.resize(1280,540)

    def update_text(self, text):
        new_text=f"<h1>{text}</h1>"
        font = QFont('Arial', 12)
        self.text_label.setFont(font)
        self.text_label.setStyleSheet('background-color: #ffffff ; border: 2px solid black ; border-radius: 10px; color: #D22E1E')
        self.text_label.setText(new_text)

    

    @pyqtSlot()
    def on_click1(self):
        if self.switch==True:
            self.dialog_frame.stop_webcam()
            self.switch=False
        else:
            self.dialog_frame.start_webcam()
            self.switch=True
    
    @pyqtSlot()
    def on_click2(self):
        self.update_text("Harsh")
        self.update_text("Aviral")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.setStyleSheet('background-color: #004879')
    widget.show()
    sys.exit(app.exec_())