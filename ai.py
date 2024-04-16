import cv2
import numpy as np
from tensorflow import keras
#
# # Загрузка предварительно обученной модели
# model = keras.models.load_model('letters_cnn_model.keras')
#
#
# def preprocess_image(image):
#     # Изменение размера изображения до 28x28 пикселей
#     resized_image = cv2.resize(image, (28, 28))
#     # Преобразование изображения в оттенки серого
#     gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
#     # Инвертирование цветов (если необходимо)
#     inverted_image = cv2.bitwise_not(gray_image)
#     # Нормализация значений пикселей
#     normalized_image = inverted_image / 255.0
#     # Расширение размерности изображения для соответствия формату входных данных модели
#     preprocessed_image = np.expand_dims(normalized_image, axis=2)
#     return preprocessed_image
#
#
# def predict_letter(image):
#     preprocessed_image = preprocess_image(image)
#     # Прогнозирование класса символа с помощью модели
#     prediction = model.predict(np.array([preprocessed_image]))
#     # Получение индекса предсказанного класса
#     predicted_class = np.argmax(prediction)
#     # Предполагаем, что A=0, B=1, и т.д., и получаем символ
#     predicted_letter = chr(predicted_class + ord('A'))
#     return predicted_letter
#
#
# # Загрузка изображения
# image_path = 'test_image.png'
# image = cv2.imread(image_path)
#
# # Предсказание символа на изображении
# predicted_letter = predict_letter(image)
# print("Predicted letter:", predicted_letter)


def print_letter(result):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXZY"
    return letters[result]


def predicting(path_to_image):
    image = keras.preprocessing.image
    model = keras.models.load_model('model.h5')

    img = image.load_img(path_to_image, target_size=(278, 278))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=1)
    result = int(np.argmax(classes))
    result = print_letter(result)
    print(result)
