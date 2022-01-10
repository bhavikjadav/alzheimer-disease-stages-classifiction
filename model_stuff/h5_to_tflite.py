import tensorflow as tf
from tensorflow.keras.models import load_model

keras_model = tf.keras.models.load_model("model_resnet50.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(keras_model)
tfmodel = converter.convert()
open ("model_resnet50.tflite" , "wb") .write(tfmodel)

# tflite_model = tf.keras.models.load_model('model.h5')
# converter = tf.lite.TFLiteConverter.from_keras_model(tflite_model)
# tflite_save = converter.convert()
# open("generated.tflite", "wb").write(tflite_save)