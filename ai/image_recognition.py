# image_recognition.py
import numpy as np
from tensorflow import keras


def predict_image(image_file):
    # Логика загрузки модели и предсказания изображения
    image = keras.preprocessing.image
    model = keras.models.load_model('model.h5')
    img = image.load_img(image_file, target_size=(278, 278))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=1)
    result = int(np.argmax(classes))
    print(result)
    return result
