# backend/predict.py

import sys
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# Load the pre-trained ResNet50 model
def load_resnet_model():
    base_model = ResNet50(weights='imagenet')
    model = Model(inputs=base_model.input, outputs=base_model.layers[-2].output)
    return model

# Load the pre-trained LSTM captioning model
def load_lstm_model():
    return load_model('models/lstm_model.h5')

# Preprocess the input image
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    return img_array

# Generate image features using the ResNet model
def extract_image_features(model, image_path):
    img_array = preprocess_image(image_path)
    features = model.predict(img_array)
    return features

# Generate a caption for the image using the LSTM model
def generate_caption(lstm_model, image_features):
    word_to_index = {'startseq': 1, 'endseq': 2}  # Update with your vocabulary
    index_to_word = {1: 'startseq', 2: 'endseq'}  # Update with your vocabulary
    max_length = 50  # Maximum length of the generated caption

    caption = 'startseq'

    for _ in range(max_length):
        sequence = [word_to_index[word] for word in caption.split() if word in word_to_index]
        sequence = pad_sequences([sequence], maxlen=max_length)

        prediction = lstm_model.predict([np.array([image_features]), np.array(sequence)])
        prediction = np.argmax(prediction)
        
        if prediction == 0:
            continue

        word = index_to_word.get(prediction, '')
        
        if word == 'endseq':
            break
        
        caption += ' ' + word
    
    return caption

# Main function to run the prediction
def predict_caption(image_path):
    resnet_model = load_resnet_model()
    lstm_model = load_lstm_model()

    image_features = extract_image_features(resnet_model, image_path)
    caption = generate_caption(lstm_model, image_features)

    return caption

if __name__ == "__main__":
    image_path = sys.argv[1]
    prediction = predict_caption(image_path)
    print(prediction)
