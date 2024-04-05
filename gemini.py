from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import streamlit as st
import os
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

question = "What is the colour of ladoo"

## Function to load OpenAI model and get respones
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

output = get_gemini_response(question)
print(output)