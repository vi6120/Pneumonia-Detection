# Keras simple code example

# 1.1 Imports
import keras
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense

print(keras.__version__)

# 1.2 Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 1.3 Normalize the input data
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255

# 1.4 Convert the labels to categorical
num_classes = 10
y_train = np_utils.to_categorical(y_train, num_classes)
y_test = np_utils.to_categorical(y_test, num_classes)

# 1.5 Create the model
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dense(num_classes, activation='softmax'))

# 1.6 Compile the model
model.compile(loss='categorical_crossentropy', 
              optimizer='adam', 
			  metrics=['accuracy'])

# 1.7 Train the model
history = model.fit(X_train.reshape(60000, 784), y_train, batch_size=128,
                    epochs=5, verbose=1, 
					validation_data=(X_test.reshape(10000, 784), y_test))
