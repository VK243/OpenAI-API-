import streamlit as st 
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Getting the key from env
openai.api_key = os.environ.get('API_KEY') ## you Openai key
openai_model = "text-davinci-002" # OpenAI model 


st.title("Text Summarizer")

st.text_area("Enter text to summarize")