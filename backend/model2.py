from tensorflow.keras.models import load_model
import tensorflow as tf
import os
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

model=load_model(r'/kaggle/input/fuly-final-model2/section_finalll.h5')# change model location

def scale_resize_image(image):
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.resize(image, (64,64))
    image=image/255.0
    image = np.expand_dims(image, axis=0)
    return (image)

import cv2
import numpy as np

img=cv2.imread(r'/kaggle/input/sections-final-dataset/sections/Wings/140_4_JPG_jpg.rf.51cf3041b30ce93dea1adf8fa5be9993.jpg')#image path

img=scale_resize_image(img)

pred=model.predict(img)

model_map=['Engine_Nacelle','Fuselage','Nose','Wings']

print("The model has predicted image as :",model_map[np.argmax(pred)])