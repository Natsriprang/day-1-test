#commit work
#setting up environment
1. create env
>python -m venv .venv
2. activate env
>source .venv/bin/activate
3. installation> create requirements.txt file
> add openai, streamlit, python-dotenv
4. install above in python
>pip install -r requirements.txt
5. create .env file
6. ensure that .env is grayed out
7. add secrets to .env : OPENAI_API_KEY="..."

#create code
1. create a python file 
>xxx.py
can create different files for different part of work
2. run streamlit
>streamlit run xxx.py
3. create code in python file
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

