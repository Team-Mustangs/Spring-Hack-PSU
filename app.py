import sys
from tkinter import Widget, dialog
from turtle import color
import cv2
from PyQt5.QtCore import Qt, QTimer, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QFrame, QLineEdit, QSpacerItem
from PyQt5.QtWidgets import QSizePolicy
import threading
import pickle
import mediapipe as mp
import pickle
import numpy as np

#footer - collaboration
'''
1) Color scheme
2) 
'''

switch=True
class CameraDialog(QDialog):

    labels_dict = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
        9: 'J',
        10: 'K',
        11: 'L',
        12: 'M',
        13: 'N',
        14: 'O',
        15: 'P',
        16: 'Q',
        17: 'R',
        18: 'S',
        19: 'T',
        20: 'U',
        21: 'V',
        22: 'W',
        23: 'X',
        24: 'Y',
        25: 'Z',
        26: 'Nothing'  ,
        27: 'Del',
        28: 'Space',
        29: "Thank you",
        30: "OK",
        31: "Not OK",
        32: "Hello"
    }

    def __init__(self):
        super().__init__()

        # Create a label to display the camera input
        self.image_label = QLabel(self)
        self.image_label.setContentsMargins(5, 5, 5, 5)
        self.image_label.resize(800, 800)
        self.image_label.setStyleSheet('background-color: #000000; border: 1px solid black ; border-radius: 10px')
        self.image_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

        # Start the camera input
        self.start_webcam()

    def update_frame(self):
        global labels_dict
        ret, frame = self.capture.read()

        if ret:
            while switch==True:

                model_dict = pickle.load(open('ASL to English\Files and Models\model.p', 'rb'))
                model = model_dict['model']

                data_aux = []
                x_ = []
                y_ = []
                
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                H, W, ch = rgb_image.shape
                bytes_per_line = ch * W

                mp_hands = mp.solutions.hands
                mp_drawing = mp.solutions.drawing_utils
                mp_drawing_styles = mp.solutions.drawing_styles

                hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

                results = hands.process(rgb_image)
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            frame,  # image to draw
                            hand_landmarks,  # model output
                            mp_hands.HAND_CONNECTIONS,  # hand connections
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())

                    for hand_landmarks in results.multi_hand_landmarks:
                        for i in range(len(hand_landmarks.landmark)):
                            x = hand_landmarks.landmark[i].x
                            y = hand_landmarks.landmark[i].y

                            x_.append(x)
                            y_.append(y)

                        for i in range(len(hand_landmarks.landmark)):
                            x = hand_landmarks.landmark[i].x
                            y = hand_landmarks.landmark[i].y
                            data_aux.append(x - min(x_))
                            data_aux.append(y - min(y_))

                    x1 = int(min(x_) * W) - 10
                    y1 = int(min(y_) * H) - 10

                    x2 = int(max(x_) * W) - 10
                    y2 = int(max(y_) * H) - 10

                    try:
                        prediction = model.predict([np.asarray(data_aux)])

                        predicted_character = labels_dict[int(prediction[0])]
                    except:
                        print("too many hands")

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                    cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                                cv2.LINE_AA)
                    
                    q_image = QImage(rgb_image.data, W, H, bytes_per_line, QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(q_image)
                    self.image_label.setPixmap(pixmap)
                    




            # Convert the frame to RGB format and display it on the label
                #rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #h, w, ch = rgb_image.shape
                #bytes_per_line = ch * w
                #frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #model_dict = pickle.load(open('ASL to English\Files and Models\model.p', 'rb'))
                #model = model_dict['model']
                #mp_hands = mp.solutions.hands
                #mp_drawing = mp.solutions.drawing_utils
                #mp_drawing_styles = mp.solutions.drawing_styles
                #hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)
                
        

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
        
        self.number=0
        self.data=["hi","I","am","not","Aviral","I","am","Ghechu"]

        self.dialog_frame = CameraDialog()

        self.text_label = QLabel("<h1>Translation</h1>", self) 
        font = QFont('Arial', 12)

        self.text_label.setFont(font)
        self.text_label.setStyleSheet('background-color: #ffffff ; border: 2px solid black ; border-radius: 10px; color: #000000; padding: 10px')
        self.text_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        button1 = QPushButton('On/Off', self)

        button1.setMinimumHeight(60)
        button1.setMaximumWidth(180)
        button1.setStyleSheet('background-color: #ffffff ; border: 2px solid black ; border-radius: 10px; color: #6B170F; padding: 10px')
        button1.clicked.connect(self.on_click1)
        button1.setFont(font)

        button2 = QPushButton('Translate', self)

        button2.setMinimumHeight(60)
        button2.setMaximumWidth(180)
        button2.setStyleSheet('background-color: #ffffff ; border: 2px solid black ; border-radius: 10px; color: #6B170F; padding: 10px')
        button2.clicked.connect(self.on_click2)
        button2.setFont(font)

        #button layout
        layout_b = QHBoxLayout()

        layout_b.addWidget(button1)
        spacer = QSpacerItem(40, 20)
        layout_b.addItem(spacer)
        layout_b.addWidget(button2)

        layout1 = QVBoxLayout()
        layout1.addWidget(self.dialog_frame)
        layout1.addLayout(layout_b)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.text_label)

        layout2.insertLayout(0, layout1)

        self.timer2=QTimer(self)
        self.timer2.timeout.connect(self.update_text)

        self.setLayout(layout2)
        self.resize(1280,540)

    def update_text(self):
        if self.number<len(self.data):
            text=self.data[self.number]
            new_text=f"<h1>{text}</h1>"
            font = QFont('Arial', 12)
            self.text_label.setFont(font)
            self.text_label.setStyleSheet('background-color: #ffffff ; border: 2px solid black ; border-radius: 10px; color: #D22E1E')
            self.text_label.setText(new_text)
            self.number+=1
        else:
            self.timer2.stop()

    @pyqtSlot()
    def on_click1(self):
        if switch==True:
            self.dialog_frame.stop_webcam()
            switch=False
        else:
            self.dialog_frame.start_webcam()
            switch=True
    
    @pyqtSlot()
    def on_click2(self):
        self.number=0
        self.timer2.start(750)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.setStyleSheet('background-color: #003252')
    widget.show()
    sys.exit(app.exec_())