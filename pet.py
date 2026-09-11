import tensorflow as tf
from tensorflow.keras import layers

# 1. Load images

train_ds = tf.keras.utils.image_dataset_from_directory(
    "dataset/train",
    image_size=(128, 128),
    batch_size=32
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    "dataset/test",
    image_size=(128, 128),
    batch_size=32
)

# 2. Preprocessing + augmentation
augmentation = tf.keras.Sequential([
    layers.Rescaling(1./255),
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.1),
    layers.RandomZoom(0.1)
])

# 3. CNN model
model = tf.keras.Sequential([
    augmentation,

    layers.Conv2D(32, 3, activation="relu"),
    layers.MaxPooling2D(),

    layers.Conv2D(64, 3, activation="relu"),
    layers.MaxPooling2D(),

    layers.Flatten(),
    layers.Dense(64, activation="relu"),
    layers.Dense(len(train_ds.class_names), activation="softmax")
])

# 4. Compile
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# 5. Train
early_stop = tf.keras.callbacks.EarlyStopping(
    monitor="val_accuracy",
    patience=3,
    restore_best_weights=True
)

model.fit(train_ds, validation_data=val_ds, epochs=10, callbacks=[early_stop])
model.save("pet_model.keras")
# 6. Predict an image
image = tf.keras.utils.load_img(
    "test.jpg",
    target_size=(128, 128)
)

x = tf.keras.utils.img_to_array(image)
x = tf.expand_dims(x, 0)

prediction = model.predict(x)
print(train_ds.class_names[tf.argmax(prediction[0])])