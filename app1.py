import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import cv2
from keras.models import load_model
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)


model =load_model('BrainTumor10EpochsCategorical.h5')
print('Model loaded. Check http://127.0.0.1:5000/')


def get_className(classNo):
	if classNo==0:
		return "No Brain Tumor"
	elif classNo==1:
		return "Yes Brain Tumor"


def getResult(img_path):
    # Load the image
    image = Image.open(img_path).convert('RGB')
    image = image.resize((64, 64))  # Resize to match the model's input shape
    image = np.array(image)
    image = image / 255.0  # Normalize pixel values to [0, 1]

    # Expand dimensions to make it a batch
    input_img = np.expand_dims(image, axis=0)

    # Predict the class
    prediction = model.predict(input_img)
    class_index = np.argmax(prediction, axis=-1)[0]  # Get the class index
    return class_index


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        value=getResult(file_path)
        result=get_className(value) 
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)