import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv
import os
import traceback

# Load environment variables from .env
load_dotenv()

# Azure OpenAI configuration
endpoint = "https://azurehubtutori7241168583.openai.azure.com/"
deployment_name = "gpt-35-turbo"  # This is your Azure deployment name (not model name!)
api_version = "2024-12-01-preview"
api_key = "2BEOSMmGYC3r9Yr5VUlhUAwKXcwSx8UhLDoQkqDPnmHpxwRVzfAWJQQJ99BEAC4f1cMXJ3w3AAAAACOGpwRt"  # Consider storing in .env

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=endpoint,
)

# Streamlit UI setup
st.set_page_config(page_title="AI Poem Generator", page_icon="📝")
st.title("🪶 AI Poem Generator")
st.markdown("Write beautiful poems with the power of Azure OpenAI!")

# User inputs
topic = st.text_input("Enter a topic for your poem:")
style = st.selectbox("Choose a style:", ["Romantic", "Funny", "Sad", "Nature", "Inspirational", "Abstract"])
length = st.slider("Number of lines:", min_value=4, max_value=20, step=2)

if st.button("Generate Poem"):
    if not topic.strip():
        st.warning("Please enter a topic before generating.")
    else:
        with st.spinner("Crafting your poem... 🎨"):
            prompt = (
                f"Write a {length}-line {style.lower()} poem about '{topic}'. "
                f"Use beautiful poetic language, vivid imagery, and creativity."
            )
            try:
                response = client.chat.completions.create(
                    model=deployment_name,  # ✅ Correct usage here
                    messages=[
                        {"role": "system", "content": "You are a poetic assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
                poem = response.choices[0].message.content
                st.success("Here's your poem:")
                st.text(poem)
            except Exception as e:
                st.error("⚠️ An error occurred:")
                st.code(traceback.format_exc())
