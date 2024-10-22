
import streamlit as st
import pandas as pd

st.title('My First Streamlit App')

# Display text
st.write("Welcome to my app!")

# Input widgets
name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")

st.image("C:\\Users\\hp\\Pictures\\Screenshots\\Correlation.png")
