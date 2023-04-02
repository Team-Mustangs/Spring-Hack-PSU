from ctypes import alignment
import sys
from tkinter import Widget, dialog
import cv2
from PyQt5.QtCore import Qt, QTimer, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QFrame, QLineEdit
from PyQt5.QtWidgets import QSizePolicy


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

        #layout = QVBoxLayout()
        #layout.minimumSize()
        dialog_frame = CameraDialog()
#
        #layout_h = QHBoxLayout()
    #
        self.text_label = QLabel("Initial text", self) 
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.resize(100,100)
#
        #layout_h.addWidget(button)
#
        #layout.addWidget(dialog_frame)
        #layout.addLayout(layout_h)
        #layout.addWidget(self.text_label)
#
        #self.setLayout(layout)1
        #self.resize(800,800)

        container_widget = QWidget(self)
        container_widget.setStyleSheet('background-color: blue')

        button1 = QPushButton('Video on', self)

        button1.setMinimumHeight(50)
        button1.setStyleSheet('background-color: green')
        button1.clicked.connect(self.on_click)

        button2 = QPushButton('Video off', self)

        button2.setMinimumHeight(50)
        button2.setStyleSheet('background-color: green')
        button2.clicked.connect(self.on_click)

        #button layout
        layout_b = QHBoxLayout()

        layout_b.addWidget(button1)
        layout_b.addWidget(button2)

        layout1 = QVBoxLayout()
        layout1.addWidget(dialog_frame)
        layout1.addLayout(layout_b)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.text_label)

        container_widget.setLayout(layout2)
        container_widget.setLayout(layout2)

        layout2.insertLayout(0, layout1)

        self.setLayout(layout2)
        self.resize(1280,720)



    
    def update_text(self):
        new_text="change"
        self.text_label.setText(new_text)

    @pyqtSlot()
    def on_click(self):
        self.update_text()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.setStyleSheet('background-color: white; border: 2px solid yellow;')
    widget.show()
    sys.exit(app.exec_())