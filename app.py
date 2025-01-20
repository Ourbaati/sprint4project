import streamlit as st
import pandas as pd

st.write("Hello")

option = st.selectbox("How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
    index=0,
    placeholder="Select contact method...",
)

st.write("You selected:", option)

