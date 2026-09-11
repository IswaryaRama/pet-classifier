import tensorflow as tf
import sys

# Load the saved model
model = tf.keras.models.load_model("pet_model.keras")

# Class names must match training order (alphabetical by default: cats, dogs)
class_names = ["cats", "dogs"]

# Get image path from command line, or default to test.jpg
image_path = sys.argv[1] if len(sys.argv) > 1 else "test.jpg"

image = tf.keras.utils.load_img(image_path, target_size=(128, 128))
x = tf.keras.utils.img_to_array(image)
x = tf.expand_dims(x, 0)

prediction = model.predict(x)
predicted_class = class_names[tf.argmax(prediction[0])]

print(f"Prediction: {predicted_class}")
