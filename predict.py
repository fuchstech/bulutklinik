import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.optimizers import Adam
# Load the saved model
model = tf.keras.models.load_model('chest_cancer_detection_model.h5',compile=False)
model.compile(loss='categorical_crossentropy',
              optimizer=Adam(learning_rate=0.001),
              metrics=['accuracy'])
# Define the class labels
class_labels = ['Adenocarcinoma', 'Large cell carcinoma', 'Squamous cell carcinoma', 'Normal']

# Load a test image from the test folder
test_image_path = 'sq.png'
test_image = image.load_img(test_image_path, target_size=(150, 150))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)

# Preprocess the test image (rescale to [0, 1])
test_image = test_image / 255.0

# Perform inference
predictions = model.predict(test_image)
predicted_class = np.argmax(predictions)

# Print the classification label
print(f'Predicted Class: {class_labels[predicted_class]}')
