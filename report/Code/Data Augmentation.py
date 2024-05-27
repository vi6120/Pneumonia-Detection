datagen = ImageDataGenerator(
 # set input mean to 0 over the dataset
featurewise_center=False, 
 # set each sample mean to 0
samplewise_center=False,  
 # divide inputs by std of the dataset
featurewise_std_normalization=False, 
  # divide each input by its std
samplewise_std_normalization=False, 
 # apply ZCA whitening
zca_whitening=False, 
 # randomly rotate images in the range (degrees, 0 to 180)
rotation_range = 30, 
 # Randomly zoom image 
zoom_range = 0.2, 
 # randomly shift images horizontally (fraction of total width)
width_shift_range=0.1,  
 # randomly shift images vertically (fraction of total height)
height_shift_range=0.1,
 # randomly flip images 
horizontal_flip = True,  
 # randomly flip images
vertical_flip=False)  
 datagen.fit(x_train)
 