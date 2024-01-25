import gradio as gr
import tensorflow as tf
#import numpy as np

model=tf.keras.models.load_model('potatoes.h5')
class_names =['Potato___Early_blight','Potato___Late_blight','Potato___healthy']

def predict(img):
    img_array = img.reshape(-1,256,256,3)
    #img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)[0]

    #predicted_class = class_names[np.argmax(predictions[0])]
    #confidence = round(100 * (np.max(predictions[0])), 2)
    return {class_names[i]: float(predictions[i]) for i in range(3)}

gr.Interface(fn=predict, inputs=gr.Image(), outputs=gr.Label(num_top_classes=3)).launch(debug='True')
     




