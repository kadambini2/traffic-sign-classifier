import streamlit as st
from PIL import Image
import numpy as np

# Page config
st.set_page_config(page_title="Traffic Sign Classifier", page_icon="🚦")

# Title
st.title("🚦 Traffic Sign Classifier")
st.write("Upload an image of a traffic sign and get prediction")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Class labels (you can expand later)
sign_names = {
    0: "Speed Limit 20 km/h",
    1: "Speed Limit 30 km/h",
    2: "Speed Limit 50 km/h",
    3: "Speed Limit 60 km/h",
    4: "Stop",
    5: "No Entry",
    6: "Yield",
    7: "No Passing",
    8: "Turn Right",
    9: "Turn Left"
}

# Dummy prediction function (replace with ML model later)
def predict_image(image):
    img = image.resize((32, 32))
    img = np.array(img)
    
    # Fake prediction (for now)
    prediction = np.random.randint(0, len(sign_names))
    return prediction

# When user uploads image
if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("🔍 Classifying...")

    prediction = predict_image(image)

    result = sign_names.get(prediction, "Unknown Sign")

    st.success(f"✅ Prediction: {result}")
       
       
