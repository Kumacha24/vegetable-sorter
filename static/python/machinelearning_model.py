import tensorflow as tf
import numpy as np
from PIL import Image

def predict_image(image):
  labels = ['ほうれん草', 'ジャガイモ', 'キャベツ', 'にんじん', 'レタス', 'たまねぎ', 'トマト']
  search_urls = ['https://www.yasainavi.com/zukan/spinach.htm', 'https://www.yasainavi.com/zukan/potato.htm', 'https://www.yasainavi.com/zukan/cabbage.htm', 
                  'https://www.yasainavi.com/zukan/carrot.htm', 'https://www.yasainavi.com/zukan/lettuce.htm', 'https://www.yasainavi.com/zukan/onion.htm', 
                  'https://www.yasainavi.com/zukan/tomato.htm']
  recipe_urls = ['https://cookpad.com/search/%E3%81%BB%E3%81%86%E3%82%8C%E3%82%93%E8%8D%89', 'https://cookpad.com/search/%E3%81%98%E3%82%83%E3%81%8C%E3%81%84%E3%82%82', 
                 'https://cookpad.com/search/%E3%82%AD%E3%83%A3%E3%83%99%E3%83%84', 'https://cookpad.com/search/%E3%81%AB%E3%82%93%E3%81%98%E3%82%93', 
                 'https://cookpad.com/search/%E3%83%AC%E3%82%BF%E3%82%B9', 'https://cookpad.com/search/%E3%81%9F%E3%81%BE%E3%81%AD%E3%81%8E', 
                 'https://cookpad.com/search/%E3%83%88%E3%83%9E%E3%83%88']
  model = tf.keras.models.load_model('static/python/my_model.h5')
  img = np.array(Image.open(image).resize((128, 128))) / 255.0
  img_expand = img[np.newaxis, ...]
  prediction_label = model.predict(img_expand)
  label_num = prediction_label[0].argmax()

  return labels[label_num], search_urls[label_num], recipe_urls[label_num]
