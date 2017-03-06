import numpy as np
#import tensorflow as tf
#import keras as kk

import matplotlib.pyplot as plt
from keras import backend as K
from keras.models import Sequential #linear stack of NN layers
from keras.layers import Dense, Dropout, Activation, Flatten #core layers
from keras.layers import Convolution2D, MaxPooling2D #conv layers for the images
from keras.utils import np_utils
from keras.datasets import mnist #mnist dataset available in keras (handwriting)
#if dataset not local it will download it 

K.set_image_dim_ordering('th')
np.random.seed(123) #for reproducability?
a = 'this is status test string'

(X_train, y_train), (X_test, y_test) = mnist.load_data() #loading mnist data

print(X_train.shape) #shows us the shape of the training data in our case
#60000 samples images and 28 by 28 pixels wide

plt.show(X_train[0]) #shows us the first sample image in the training dataset
plt.show(X_train[1])


#When using the Theano backend, you must explicitly declare a dimension
#for the depth of the input image. For example, a full-color image with
#all 3 RGB channels will have a depth of 3.

#Our MNIST images only have a depth of 1, but we must explicitly declare that.

#In other words, we want to transform our dataset from having shape
#(n, width, height) to (n, depth, width, height).

X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)

# to confirm and see if it worked
print(X_train.shape)

#The final preprocessing step for the input data is to convert our data type to
#float32 and normalize our data values to the range [0, 1].

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

#now the data is ready for model training

print(a)

#take a look at the class labels
print(y_train.shape)

#Hmm... that may be problematic. We should have 10 different classes,
#one for each digit, but it looks like we only have a 1-dimensional array.
#Let's take a look at the labels for the first 10 training samples:

print(y_train[:10])

#And there's the problem. The y_train and y_test data are not split
#into 10 distinct class labels, but rather are represented as a single
#array with the class values.

# Convert 1-dimensional class arrays to 10-dimensional class matrices
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

#test and see again
print(Y_train.shape)

#Now all set - we need to define our model architechture now! Lots of research
#many architechtures available on keras website

#We use sequential now

model = Sequential()

#declare the input layer
model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(1,28,28)))

#The input shape parameter should be the shape of 1 sample.
#In this case, it's the same (1, 28, 28) that corresponds to
#the (depth, width, height) of each digit image.

#But what do the first 3 parameters represent?
#They correspond to the number of convolution filters to use,
#the number of rows in each convolution kernel,
#and the number of columns in each convolution kernel, respectively.

#confirm by printing out the shape of the model
print(model.output_shape)

#add more layers to the model

model.add(Convolution2D(32, 3, 3, activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

#the Dropout layer we just added. This is a method for
#regularizing our model in order to prevent overfitting.

#MaxPooling2D is a way to reduce the number of parameters
#in our model by sliding a 2x2 pooling filter
#across the previous layer and taking the max of the 4 values
#in the 2x2 filter.

#So far, for model parameters, we've added two Convolution layers.
#To complete our model architecture, let's add a fully connected
#layer and then the output layer:

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

#For Dense layers, the first parameter is the output size of the
#layer. Keras automatically handles the connections between layers.

#Note that the final layer has an output size of 10, corresponding
#to the 10 classes of digits.

#Also note that the weights from the Convolution layers must be flattened
#(made 1-dimensional) before passing them to the fully connected Dense layer.

###########
# FIXES ERROR -1 in SHAPE need to look this up !
# from keras import backend as K
# K.set_image_dim_ordering('th')
#
###########


#Now all we need to do is define the loss function and the optimizer,
#and then we'll be ready to train it.


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

#To fit the model, all we have to do is declare the batch size and number
#of epochs to train for, then pass in our training data.

model.fit(X_train, Y_train, 
          batch_size=32, nb_epoch=2, verbose=1)

#You can also use a variety of callbacks to set early-stopping rules,
#save model weights along the way, or log the history of each training epoch.

#Finally, we can evaluate our model on the test data:

score = model.evaluate(X_test, Y_test, verbose=1)

print(score)
