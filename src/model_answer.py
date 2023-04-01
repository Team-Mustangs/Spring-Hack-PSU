import cv2
import numpy as np
import tensorflow as tf

# Load the pre-trained model
model = tf.keras.models.load_model('path/to/model.h5')

# Define the labels for the objects we want to detect
labels = ['car', 'person', 'dog', 'cat', 'bird']

# Initialize the video capture device
cap = cv2.VideoCapture(0)

# Set the width and height of the video capture
cap.set(3, 640)
cap.set(4, 480)

# Define a function to preprocess the video frames for input to the model
def preprocess_frame(frame):
    # Resize the frame to the input size of the model
    frame = cv2.resize(frame, (224, 224))
    # Convert the frame to a numpy array and normalize the pixel values
    frame = np.array(frame, dtype=np.float32) / 255.0
    # Add an extra dimension to represent the batch size of 1
    frame = np.expand_dims(frame, axis=0)
    return frame

# Loop over the frames in the live video feed
while True:
    # Read a frame from the video capture device
    ret, frame = cap.read()

    # Preprocess the frame for input to the model
    input_frame = preprocess_frame(frame)

    # Make a prediction with the model
    prediction = model.predict(input_frame)

    # Find the label with the highest predicted probability
    predicted_label = labels[np.argmax(prediction)]

    # Draw the label on the frame
    cv2.putText(frame, predicted_label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the frame in a window
    cv2.imshow('Live Feed', frame)

    # Wait for a key press and check if it's the 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close the window
cap.release()
cv2.destroyAllWindows()
