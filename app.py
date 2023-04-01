import sys
import cv2
import numpy as np
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout

class CameraDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Create a label to display the camera input
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Create a label to display the finger count output
        self.finger_label = QLabel(self)
        self.finger_label.setAlignment(Qt.AlignCenter)
        self.finger_label.setText("No fingers detected")

        # Set up the layout for the dialog
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.finger_label)
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

            # Process the image and update the finger label
            finger_count = self.process_image(frame)
            self.finger_label.setText(f"{finger_count} fingers detected")

    def process_image(self, frame):
        # Convert the frame to grayscale and blur it to remove noise
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (11, 11), 0)

        # Threshold the image to isolate the hand
        _, thresh = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)

        # Find contours in the thresholded image
        contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # If no contours are found, return 0 fingers
        if len(contours) == 0:
            return 0

        # Find the largest contour, which should be the hand
        max_contour = max(contours, key=cv2.contourArea)

        # Create a bounding rectangle around the hand
        x, y, w, h = cv2.boundingRect(max_contour)

        # Extract the hand region of interest and resize it to a fixed size
        roi = gray[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))

        # Threshold the hand region of interest to isolate the fingers
        _, thresh_roi = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Find contours in the thresholded hand region of interest
        contours_roi, hierarchy_roi = cv2.findContours(thresh_roi.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # If no contours are found in the hand region of interest, return 0 fingers
        if len(contours_roi) == 0:
            return 0

        # Find the contour with the
        max_contour_roi = max(contours_roi, key=cv2.contourArea)

        # Count the number of fingers based on the number of convexity defects in the hand region of interest
        hull = cv2.convexHull(max_contour_roi, returnPoints=False)
        defects = cv2.convexityDefects(max_contour_roi, hull)

        if defects is None:
            return 0

        finger_count = 0
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(max_contour_roi[s][0])
            end = tuple(max_contour_roi[e][0])
            far = tuple(max_contour_roi[f][0])

            # Ignore defects that are too close to the edge of the hand region of interest
            if d < 200:
                continue

            # Compute the angle between the finger and the palm
            angle = np.degrees(np.arctan2(far[1] - start[1], far[0] - start[0]) - np.arctan2(end[1] - start[1], end[0] - start[0]))
            if angle < 0:
                angle += 180

            # If the angle is within the range of a finger, count it
            if angle > 20 and angle < 160:
                finger_count += 1

        return finger_count


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = CameraDialog()
    dialog.show()
    sys.exit(app.exec_())