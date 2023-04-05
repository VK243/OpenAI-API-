import streamlit as st 
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Getting the key from env
openai.api_key = os.environ.get('API_KEY') ## you Openai key


st.title("Keywords Extractor")
text = st.text_area("Enter Text:")




def generate(text):
    model = "text-davinci-002" # OpenAI model 
    k_prompt = f"Extract the Keywords from this text:\n\n"+str(text)+"\n\nThe keywords must be accurate."
    response = openai.Completion.create(
        engine = model,
        prompt = k_prompt,
        temperature = 0.7,
        max_tokens = 200,
        top_p = 1.0,
        # frequency_penalty=0.8,
        # presence_penalty=0.0,
    )
    
    keywords = response.choices[0].text
    return keywords
    

if st.button("Generate"):
    keyword = generate(text) 
    st.write(keyword)  

