import streamlit as st
from google import genai
from PIL import Image
import os

# Configure the Streamlit page layout
st.set_page_config(page_title="Gemini Image Captioner", page_icon="🖼️", layout="centered")

st.title("🖼️ Gemini Image Caption Generator")
st.write("Upload an image, and Gemini will generate a descriptive caption for it.")

# --- API KEY SETUP ---
# Securely fetch the API key from Streamlit secrets, environment variables, or user input.
# For local testing, you can create a .streamlit/secrets.toml file with GEMINI_API_KEY="your_key"
api_key = st.secrets.get("GEMINI_API_KEY", os.environ.get("GEMINI_API_KEY"))

if not api_key:
    st.info("Please enter your Gemini API key to continue. Get one at [Google AI Studio](https://aistudio.google.com/).")
    api_key = st.text_input("Gemini API Key", type="password")

# --- MAIN APP LOGIC ---
if api_key:
    # Initialize the new Google GenAI client
    client = genai.Client(api_key=api_key)
    
    # Create a file uploader restricting to common image types
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])
    
    if uploaded_file is not None:
        # Open the image using Pillow and display it
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        # Trigger generation only when the user clicks the button
        if st.button("Generate Caption"):
            with st.spinner("Analyzing image..."):
                try:
                    # Pass both the text instruction and the PIL image object to Gemini
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=[
                            "Write a detailed, descriptive caption for this image.",
                            image
                        ]
                    )
                    
                    # Display the result
                    st.subheader("Generated Caption")
                    st.success(response.text)
                    
                except Exception as e:
                    st.error(f"An error occurred with the Gemini API: {e}")  