import sys
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array


# Load pre-trained models
model = load_model('model.keras')  
resnet = load_model("resnet.keras")