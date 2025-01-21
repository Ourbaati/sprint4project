import streamlit as st
import pandas as pd
st.title('Car Dataset Feature Explorer')

options = ['Price', 'Odometer', 'Condition', 'Days Listed']

selected_option = st.selectbox('Select a feature to analyze:', options)

st.write("You selected:", selected_option)

