import tensorflow as tf
import numpy as np
from PIL import Image

train_size = 2000
num = []
for i in range(10):
    img = Image.open("code/{}.png".format(i))
    num.append(np.asarray(img, dtype=np.float32))

x_train, y_train = np.zeros(shape=(train_size, 20, 15)), np.zeros(shape=(train_size,))
for i in range(train_size):
    n = np.random.randint(10)
    y_train[i] += n
    x_train[i] += num[n]

x_train = x_train / 255.0
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(20, 15)),
    tf.keras.layers.Dense(512, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)
model.save('my_model.h5')
