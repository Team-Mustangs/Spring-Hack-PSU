import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Dropout

params = {
    'dropout': 0.25,
    'batch-size': 128,
    'epochs': 50,
    'layer-1-size': 128,
    'layer-2-size': 128,
    'initial-lr': 0.01,
    'decay-steps': 2000,
    'decay-rate': 0.9,
    'optimizer': 'adamax'
}

mnist = tf.keras.datasets.mnist  
num_class = 10

# split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# reshape and normalize the data
x_train = x_train.reshape(60000, 784).astype("float32")/255
x_test = x_test.reshape(10000, 784).astype("float32")/255

# convert class vectors to binary class matrices
y_train = to_categorical(y_train, num_class)
y_test = to_categorical(y_test, num_class)

