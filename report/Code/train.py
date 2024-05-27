import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dropout, Flatten, Dense
from tensorflow.keras.layers import Activation, BatchNormalization, add
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import plot_model
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
import os

# Set the author as "Vikas Ramaswamy"
__author__ = "Vikas Ramaswamy"

# Set the base directory
base_dir = "/Users/vikasramaswamy/Desktop/BusinessAnalytics/App/DataSet/chest_xray"

# Set the target shape for input images
target_shape = (224, 224)

# Set the directories for training, validation, and test data
train_dir = os.path.join(base_dir, "train")
val_dir = os.path.join(base_dir, "val")
test_dir = os.path.join(base_dir, "test")

# Load the VGG16 model with ImageNet weights 
# without the fully connected layers
vgg = VGG16(weights='imagenet',
             include_top=False, input_shape=(224, 224, 3))

# Set all the layers in the VGG16 model as non-trainable
for layer in vgg.layers:
    layer.trainable = False

# Flatten the output from the VGG16 model
x = Flatten()(vgg.output)

# Add a fully connected (dense) layer for binary classification 
# (2 classes: pneumonia and healthy)
predictions = Dense(2, activation='softmax')(x)

# Create the final model by specifying the input and output layers
model = Model(inputs=vgg.input, outputs=predictions)

# Print the summary of the model
model.summary()

# Create an ImageDataGenerator for data augmentation 
# and normalization on the training data
train_gen = ImageDataGenerator(rescale=1/255.0,
                               horizontal_flip=True,
                               zoom_range=0.2,
                               shear_range=0.2)

# Create an ImageDataGenerator for normalization on the test data
test_gen = ImageDataGenerator(rescale=1/255.0)

# Create iterable objects for training and validation data 
# using the respective data directories
train_data_gen = train_gen.flow_from_directory(train_dir,
                                               target_shape,
                                               batch_size=16,
                                               class_mode='categorical')

test_data_gen = train_gen.flow_from_directory(test_dir,
                                              target_shape,
                                              batch_size=16,
                                              class_mode='categorical')

# Save a visualization of the model architecture to a file
plot_model(model, to_file='model.png')

# Compile the model with appropriate loss function,
#  optimizer, and evaluation metric
model.compile(loss='categorical_crossentropy', 
              optimizer='adam', metrics=['accuracy'])

# Train the model using the training data and 
# validate using the validation data
hist = model.fit_generator(train_data_gen,
                           steps_per_epoch=20,
                           epochs=20,
                           validation_data=test_data_gen,
                           validation_steps=10)

# Plot the training loss, validation loss, 
# training accuracy, and validation accuracy
plt.style.use("ggplot")
plt.figure()
plt.plot(hist.history["loss"], label="train_loss")
plt.plot(hist.history["val_loss"], label="val_loss")
plt.plot(hist.history["accuracy"], label="train_acc")
plt.plot(hist.history["val_accuracy"], label="val_acc")
plt.title("Model Training")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.savefig("epochs.png")

# Save the trained model to a file
model.save('model.h5')
