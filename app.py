import streamlit as st
import os
import google.generativeai as genai
from apikey import google_gemini_apikey
from google.generativeai.types import HarmCategory, HarmBlockThreshold
genai.configure(api_key="AIzaSyCEP96aT3ZSa9woFyFKgTUT5Lyl1lltonI")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = {
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}




st.set_page_config(layout='wide')
st.title('Blogilatte: Your AI Writing Companion')
st.subheader('Brew your blogs in the blink of an eye with Blogilatte:Your AI Writing Companion')

with st.sidebar:
    st.title("Input your Blog Details:")
    st.subheader('Enter the blog details you want to generate')

    Blog_title=st.text_input("Blog Title")

    keywords=st.text_area("Keywords (comma_seperated)")
    num_words=st.slider("Number of Words",min_value=250,max_value=1000,step=250)
    num_images=st.number_input("Number of Images",min_value=1,max_value=5,step=1)

    submit_button=st.button("Generate Blog")

if submit_button:
    # Start the chat session and generate the blog content
    chat_session = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=generation_config,
        safety_settings=safety_settings
    ).start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    f"Generate a comprehensive and engaging blog relevant to the title \"{Blog_title}\" "
                    f"with keywords \"{keywords}\". Make sure to incorporate the keywords in the blog post. "
                    f"The blog should be approximately {num_words} words in length and suitable for an online audience. "
                    f"Ensure that the post is original, informative, and maintains a consistent tone throughout."
                ]
            }
        ]
    )

    # Send the constructed message and display the response
    response = chat_session.send_message(
        f"Please generate a blog for the title: '{Blog_title}' with the keywords: '{keywords}' in around {num_words} words.")

    st.write(response.text)
