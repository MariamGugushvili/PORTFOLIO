# -*- coding: utf-8 -*-
"""+++Task1c(after-tuning).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vRRFpRR-STI9yyIm7tjwiUYjZ2DZRO6B
"""

import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.callbacks import LearningRateScheduler

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

base_model = VGG16(weights='imagenet', include_top=False, input_shape=(32, 32, 3))

for layer in base_model.layers[-5:]: layer.trainable = True

x = base_model.output
x = Flatten()(x)
x = Dense(256, activation='relu')(x)
predictions = Dense(10, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)
model.summary()

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

layer_weights = model.get_layer('block1_conv1').get_weights()[0]

filter_height, filter_width, in_channels, out_channels = layer_weights.shape
num_filters_to_display = 32  # Choose the number of filters to display
filters = layer_weights[:, :, :, :num_filters_to_display]

# Visualize the filters
plt.figure(figsize=(10, 10))
for i in range(num_filters_to_display):
    plt.subplot(8, 4, i+1)  # Adjust subplot layout if needed

    # Select the first channel (or any specific channel) for visualization
    # You can experiment with different channels
    filter_to_display = filters[:, :, 0, i]

    # Display the filter, normalizing values for visualization
    plt.imshow(filter_to_display.astype(np.float32), cmap='YlGn')
    plt.axis('off')
plt.show()

layer_name = 'block1_conv1'  # Choose a layer
layer_output = model.get_layer(layer_name).output
intermediate_model = Model(inputs=model.input, outputs=layer_output)

# Get feature maps for a sample image
img = x_test[10]
img = np.expand_dims(img, axis=0)
feature_maps = intermediate_model.predict(img)

# Visualize the feature maps - adjust the grid size
# Calculate grid dimensions based on the number of feature maps
grid_size = int(np.ceil(np.sqrt(feature_maps.shape[-1])))

plt.figure(figsize=(10, 10))
for i in range(feature_maps.shape[-1]):
    # Use grid_size x grid_size to accommodate all feature maps
    plt.subplot(grid_size, grid_size, i+1)
    plt.imshow(feature_maps[0, :, :, i], cmap='turbo')
    plt.axis('off')
plt.show()

# Evaluate the model and get predictions
loss, accuracy = model.evaluate(x_test, y_test)

# Get predicted probabilities
y_pred_probs = model.predict(x_test)
# Get the class with the highest probability
y_pred = np.argmax(y_pred_probs, axis=1)

# Calculate Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# Calculate Precision, Recall, and F1-score
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print("Classification Report:\n", report)

import matplotlib.pyplot as plt

# Assuming you have training and validation loss histories
train_loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(train_loss) + 1)

plt.plot(epochs, train_loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()