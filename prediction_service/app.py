import streamlit as st
import pandas as pd
from PIL import Image
import tensorflow as tf
import numpy as np

'''
# deep Classifier project 

'''
model = tf.keras.models.load_model("model.h5")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # To read file as bytes:
    image = Image.open(uploaded_file)
    img = image.resize((224,224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0) # [batch_size, row, col, channel] --> expands row wise as axis=0 .i.e additional dim is added in a row
    result = model.predict(img_array) # [[0.99, 0.01], [0.99, 0.01]], if passed two images o/p will be of this form.
    
    argmax_index = np.argmax(result, axis=1) # i/p [0.99, 0.01] --> o/p[0 ,0] argmax returns index that has highest value, axis=1 means checks col wise
    if argmax_index[0] == 0:
        st.image(image, caption="predicted: cat")
    else:
        st.image(image, caption="predicted: dog")

