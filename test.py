import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

st.header("TEST DAY 1")
st.title("Environment creation")
name = st.text_input("What is your name?")
if "name" not in st.session_state:
    st.session_state.name = ""
if st.button("Click"):
    if name == "Nat":
        st.write("Welcome back")
    else:
        st.write("You cannot come in here!")

client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    input=f"write a greetings to {name}."       
)
st.write(response.output_text)


