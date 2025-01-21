import streamlit as st
import pandas as pd

# Load the data
file_path = 'C:/Users/youss/OneDrive/Desktop'
vehicles_df = pd.read_csv('file_path')

# Streamlit app
st.title("Vehicle Data Analysis")

# Dropdown for column selection
st.header("Select a Column")
columns = ['price', 'model_year', 'model', 'odometer']
selected_column = st.selectbox("Select a column:", columns)

# Display the selected column
def display_column_info(column):
    st.write(f"You selected: {column}")
    st.write(vehicles_df[column].head())

if selected_column:
    display_column_info(selected_column)
