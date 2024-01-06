import streamlit as st
import requests
from openai import OpenAI

apiKey = "YOUR_API_KEY"
OpenAI.api_key = apiKey

endpoint = "https://api.openai.com/v1/completions"

st.header("GPT 3.5")
st.write("Currentlly, this project is working on top of GPT-3.5.")

st.write(""" 
         
         Ask Question and get answer quickly
         
         """)


prompt = st.text_area("Ask your query here", placeholder='Type here ...')

# prompt = "how are you doing"

askButton = st.button("Ask Now")

parameters = {
    'model': "gpt-3.5-turbo-instruct",
    # 'model': "davinci-002",
    'prompt': prompt,
    'max_tokens':500,
}

if askButton:
    response = requests.post(endpoint, json=parameters, headers={"Authorization": f'Bearer {apiKey}'})

    if response.status_code == 200:
        result = response.json()
        text = result['choices'][0]['text']
        st.write(text)
    else:
        st.write(f"Error: {response.status_code}\n{response.text}")
        # print(f"Error: {response.status_code}\n{response.text}")



# response = requests.post(endpoint, json=parameters, headers={"Authorization": f'Bearer {apiKey}'})

# if response.status_code == 200:
#     result = response.json()
#     text = result['choices'][0]['text']
    
# else:
#     print(f"Error: {response.status_code}\n{response.text}")
