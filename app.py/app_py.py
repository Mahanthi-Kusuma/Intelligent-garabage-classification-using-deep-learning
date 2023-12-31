# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13kwbltnSwjkhFGs6bOhndRr_eAXA7YuG
"""

from flask import Flask, jsonify, render_template, request
from keras.models import load_model
from PIL import Image
import numpy as np
import os
import io

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

print("Checking backend Garbage Classifier Model")
model_filename = (os.path.join(os.getcwd(),'model','Garbage3.h5'))
print(model_filename)
model = load_model(model_filename)

@app.route('/')
def home():
    return render_template('index1.html')

@app.route('/classify')
def classify():
    return render_template('classify.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print(request.form)
        img = request.files['file'].read()
        img = Image.open(io.BytesIO(img))
        img = img.resize((64, 64))
        img_array = np.array(img) / 255.
        img_array = np.expand_dims(img_array, axis=0)
        pred = model.predict(img_array)[0]
        class_idx = np.argmax(pred)
        class_names = ['Cardboard','Glass','Metal','paper','Plastic','Trash']
        predicted_class = class_names[class_idx]
        return f"'Given Waste is a': {predicted_class}"
    except:
         return ("Invalid Input")

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/about')
def about():
    return render_template('about1.html')

if __name__ == '__main__':
    app.run(host = '127.0.0.1',port = 5000, debug = False)