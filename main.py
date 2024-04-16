# import os
# import cv2
# import numpy as np
# from tensorflow import keras
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
#
#
# # Функция для загрузки изображений и их меток
# def load_data(folder_path):
#     images = []
#     labels = []
#     # Получаем список подпапок (букв)
#     folders = os.listdir(folder_path)
#     for folder in folders:
#         # Получаем список файлов в папке
#         files = os.listdir(os.path.join(folder_path, folder))
#         for file in files:
#             # Загружаем изображение
#             image = cv2.imread(os.path.join(folder_path, folder, file), cv2.IMREAD_GRAYSCALE)
#             # Предварительная обработка изображения (если необходимо)
#             # Например, масштабирование, нормализация, изменение размера и т.д.
#             image = cv2.resize(image, (28, 28))
#             # Добавляем изображение и его метку в списки
#             images.append(image)
#             labels.append(ord(folder) - ord('A'))  # Преобразуем символ в число (A=0, B=1, ...)
#     return np.array(images), np.array(labels)
#
#
# # Путь к папке с изображениями букв
# folder_path = "Latin"
# # Загружаем изображения и их метки
# x_train, y_train = load_data(folder_path)
#
# # Нормализация данных
# x_train = x_train.astype('float32') / 255.0
#
# # Преобразование меток в one-hot encoding
# y_train = keras.utils.to_categorical(y_train, num_classes=26)  # 26 букв в алфавите
#
#
# # Создание модели сверточной нейронной сети
# model = Sequential([
#     Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
#     MaxPooling2D(pool_size=(2, 2)),
#     Flatten(),
#     Dense(128, activation='relu'),
#     Dense(26, activation='softmax')  # 26 букв в алфавите
# ])
#
# # Компиляция модели
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#
# # Обучение модели
# model.fit(x_train, y_train, batch_size=256, epochs=20, verbose=1, validation_split=0.2)
#
#
# # Сохранение модели
# model.save('letters_cnn_model.keras')

import tensorflow as tf
ImageDataGenerator = tf.keras.preprocessing.image.ImageDataGenerator
TRAINING_DIR = "Latin"
train_datagen = ImageDataGenerator(rescale=1.0 / 255.)
train_generator = train_datagen.flow_from_directory(TRAINING_DIR,
                              batch_size=40,
                              class_mode='binary',
                              target_size=(278,278))

VALIDATION_DIR = "Latin-test"
validation_datagen = ImageDataGenerator(rescale=1.0 / 255.)
validation_generator = validation_datagen.flow_from_directory(VALIDATION_DIR,
                                      batch_size=40,
                                      class_mode='binary',
                                      target_size=(278,278))

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu',
                           input_shape=(278,278, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(33, activation='softmax')
])
model.compile(optimizer='adam',
loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()
history = model.fit_generator(train_generator,
                           epochs=2,
                           verbose=1,
                           validation_data=validation_generator)

model.save('model.h5')