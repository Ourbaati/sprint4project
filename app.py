import streamlit as st
import pandas as pd

# Load the data
file_path = 'vehicles_us.csv'
data = pd.read_csv('C:/Users/youss/OneDrive/Desktop/sprint4project/notebook')

# Streamlit app
st.title("Vehicle Data Analysis")

# Dropdown for column selection
st.header("Select a Column")
columns = data.columns.tolist()
selected_column = st.selectbox("Select a column:", columns)

# Display the selected column
def display_column_info(column):
    st.write(f"You selected: {column}")
    st.write(data[column].head())

if selected_column:
    display_column_info(selected_column)
