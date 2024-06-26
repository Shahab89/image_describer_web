import json
import os
import streamlit as st
import requests
import pandas as pd
from PIL import Image , UnidentifiedImageError
import io



#API_URL = os.environ.get('API_URL')
API_URL = 'http://127.0.0.1:8000/'  # Update with your API URL


ERROR_MESSAGE_TEMPLATE = """
Could not get {requested}

{error}
"""
# Initialize session state variables
if 'image' not in st.session_state:
    st.session_state.image = None
if 'language' not in st.session_state:
    st.session_state.language = ''
if 'description' not in st.session_state:
    st.session_state.description = ''
if 'audio_file' not in st.session_state:
    st.session_state.audio_file = None


st.set_page_config(page_title="Intelligent Image Describer", page_icon="🖼️", layout="wide")

st.header("Intelligent Image Describer 🖼️ ✍️ 🔊")
st.header("🖼️ Choose an image...")
uploaded_image = st.file_uploader('', type=["jpg", "jpeg", "png"])

# Check if a file has been uploaded
if uploaded_image is not None:
    try:
        # Open the image file

        # Read the uploaded file as bytes
        image_bytes = uploaded_image.getvalue()
        # Convert the bytes to a file-like object
        st.session_state.image = Image.open(io.BytesIO(image_bytes))


        # Create a file-like object to send in the POST request
        files = {'image': (uploaded_image.name, image_bytes, uploaded_image.type)}

        # Send the image to the FastAPI endpoint
        response = requests.post(API_URL + 'upload_image', files=files)
        # Display the image
        st.image(st.session_state.image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.success("Image uploaded successfully! 🎉")
    except UnidentifiedImageError:
        st.error("The uploaded file is not a valid image. Please upload a valid image file (jpg, jpeg, png).")
# Add a message for the user
else:
    st.warning("⚠️ Please upload an image file.")



def fetch_description():
    params_dict = {
        'language': st.session_state.language
    }
    response = requests.get(API_URL+'description', params= params_dict)
    return response.text


st.header("Sellect Language")
language =  st.selectbox('Select a line to filter', ['English', 'German'])
if st.button('Select'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    st.session_state.language = language
    st.session_state.description = fetch_description()
st.markdown(f"#### ✍️ Image Description: \n{ st.session_state.description} ")


# Function to generate audio from description
def fetch_audio(language):
    response = requests.get(API_URL + 'speech', params={'language': language}, stream=True)
    if response.status_code == 200:
        return response.content
    else:
        return None

# Button to generate audio
if st.button('🔊 Generate Audio'):
    if st.session_state.description is not None:
        audio_response = fetch_audio(st.session_state.language)
        if audio_response:
            st.session_state.audio_file = audio_response
            st.success("Audio successfully saved and ready to play!  🎉")
        else:
            st.error("Failed to generate audio. Please try again. 😕")
    else:
        st.warning("⚠️ Please upload an image and generate its description first.")

# Play the audio if available
if st.session_state.audio_file:
    st.audio(st.session_state.audio_file, format='audio/mpeg')
