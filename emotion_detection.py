import cv2
import numpy as np
from PIL import Image

# Load the ONNX model
model_path = "emotion-ferplus-2.onnx"
model = cv2.dnn.readNetFromONNX(model_path)

# Define the preprocessing function
def preprocess(image_path):
    input_shape = (1, 1, 64, 64)
    img = Image.open(image_path)
    img = img.convert("L")
    img = img.resize((64, 64), Image.LANCZOS)
    img_data = np.array(img) / 255.0
    img_data = np.reshape(img_data, input_shape)
    return img_data

# Preprocess the image
image_path = "image1.jpg"
blob = preprocess(image_path)

# Set the input for the model
model.setInput(blob)

# Run inference
output = model.forward()

# Define emotion labels
emotions = ["neutral", "happiness", "surprise", "sadness", "anger", "disgust", "fear", "contempt"]

# Get the predicted emotion
emotion_index = np.argmax(output[0])
predicted_emotion = emotions[emotion_index]
print(f"Predicted Emotion: {predicted_emotion}")
