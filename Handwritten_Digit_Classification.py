# Handwritten Digit Classification using Neural Networks

# Import libraries
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build Neural Network model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),   # Input layer
    layers.Dense(128, activation='relu'),   # Hidden layer
    layers.Dense(64, activation='relu'),    # Hidden layer
    layers.Dense(10, activation='softmax')  # Output layer
])

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train model
history = model.fit(x_train, y_train, epochs=5, validation_split=0.2)

# Evaluate model
test_loss, test_acc = model.evaluate(x_test, y_test)

print("\nTest Accuracy:", test_acc)

# Predict on test data
predictions = model.predict(x_test)

# Display some predictions
for i in range(5):
    plt.imshow(x_test[i], cmap='gray')
    plt.title(f"Predicted: {predictions[i].argmax()} | Actual: {y_test[i]}")
    plt.axis('off')
    plt.show()