import tensorflow as tf
import numpy as np
from PIL import Image

def predict_image(image):
  labels = ['ほうれん草', 'ジャガイモ', 'キャベツ', 'にんじん', 'レタス', 'たまねぎ', 'トマト']
  model = tf.keras.models.load_model('static/python/my_model.h5')
  img = np.array(Image.open(image).resize((128, 128))) / 255.0
  img_expand = img[np.newaxis, ...]
  
  prediction_label = model.predict(img_expand)
  label_num = prediction_label[0].argmax()

  return labels[label_num]
