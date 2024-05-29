import os
import logging
from dotenv import load_dotenv


import streamlit as st
from openai import OpenAI

from decorator import error_handler

from constant import WRITE_PROPERLY_PROPERLY_DEFAULT_PROMPT, FIX_GRAMMAR_DEFAULT_PROMPT, SUMARIZE_DEFAULT_PROMPT, \
                    WRITE_PROPERLY_PROPERLY_DEFAULT_CONTEXT, FIX_GRAMMAR_DEFAULT_CONTEXT, SUMARIZE_DEFAULT_CONTEXT
load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


OPEN_API_KEY = os.getenv('OPEN_API_KEY')
LLM_MODEL = os.getenv('LLM_MODEL')

### Setting Streamlit configuration options for creating a title and page layout
st.set_page_config(page_title="OpenAI Text Processing", layout="wide")

### Initializing OpenAI client with apikey. Kindly replace it with your own key 
client = OpenAI(api_key=OPEN_API_KEY)


# This function Enhances both grammar and style of the input message
@error_handler
def write_properly(user_input: str) -> str:
    prompt = f"{WRITE_PROPERLY_PROPERLY_DEFAULT_PROMPT} {user_input}"
    completion = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": WRITE_PROPERLY_PROPERLY_DEFAULT_CONTEXT},
            {"role": "user", "content": prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response


# This function Corrects only the grammatical errors in the input message
@error_handler
def write_the_same_grammar_fixed(user_input: str) -> str:
    prompt = f"{FIX_GRAMMAR_DEFAULT_PROMPT} {user_input}"
    completion = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": FIX_GRAMMAR_DEFAULT_CONTEXT},
            {"role": "user", "content": prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response
 
# This function Provides a concise summary of the input message 
@error_handler
def summarize(user_input: str) -> str:
    prompt = f"{SUMARIZE_DEFAULT_PROMPT} {user_input}"
    completion = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": SUMARIZE_DEFAULT_CONTEXT},
            {"role": "user", "content": prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response   