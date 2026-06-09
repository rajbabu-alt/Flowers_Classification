import gradio as gr
import tensorflow as tf
from PIL import Image
import numpy as np

model = tf.keras.models.load_model('flower_classifier_fixed.keras')
flowers = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

def predict(image):
    img = Image.fromarray(image).resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array,0)
    prediction = model.predict(img_array)
    result = {flowers[i]: float(prediction[0][i]) for i in range(5)}
    return result

gr.Interface(
    fn=predict,
    inputs = gr.Image(),
    outputs = gr.Label(num_top_classes=5),
    title = "Flower_Classifier_By_RajBabu"
).launch()
