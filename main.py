import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class generate_response():
    def __init__(self) -> None:
       self.model=genai.GenerativeModel("gemini-pro-vision")
        
    def response(self,input,image,prompt):
        return self.model.generate_content([input,image[0],prompt]).text
    def input_image_setup(self,upload_file=None):
        if upload_file !=None:
            bytes_data=upload_file.getvalue()
            image_parts=[
                {
                    "mime_type":upload_file.type,
                    "data":bytes_data
                }
            ]
            return image_parts
        else:
            raise FileNotFoundError("NO file  has been Uploaded")


# Initalizing the Streamlit Frontend App
        
st.set_page_config(page_title="Callories Calculator")
st.header("Calories Advisor App")
input=st.text_input("Input Promt::",key="input")
uploaded_files=st.file_uploader(" Give the Image Input :::",type=["jpg","jpeg","png"])

image=""

if uploaded_files !=None:
    image=Image.open(uploaded_files)
    st.image(image,caption='This is the Uploaded File',use_column_width= True)
submit=st.button("Give me the Callories Count")


input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----

Also advise me to loosing the Weight Should i eat this or not


"""


if submit:
    obj=generate_response()
    image_data=obj.input_image_setup(upload_file=uploaded_files)
    response=obj.response(input=input_prompt,image=image_data,prompt=input)
    st.subheader("The Response is")
    st.write(response)