import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = 'vehicles_us.csv'
vehicles_df = pd.read_csv('C:/Users/youss/OneDrive/Desktop/vehicles_us.csv')

# Streamlit app
st.title("Vehicle Data Analysis")

# Display dataset
st.header("Dataset Overview")
st.write(data.head())

# Dropdown for column selection
st.header("Select Columns for Analysis")
columns = ['price', 'condition', 'odometer']
selected_column = st.selectbox("Select a column for histogram:", columns)

# Histogram
st.header("Histogram")
if selected_column:
    st.subheader(f"Histogram of {selected_column}")
    fig, ax = plt.subplots()
    ax.hist(data[selected_column].dropna(), bins=30, edgecolor='k')
    ax.set_title(f"Distribution of {selected_column}")
    ax.set_xlabel(selected_column)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

# Scatterplot
st.header("Scatterplot")
x_column = st.selectbox("Select X-axis column:", columns, index=0)
y_column = st.selectbox("Select Y-axis column:", columns, index=1)
if x_column and y_column:
    st.subheader(f"Scatterplot of {x_column} vs. {y_column}")
    fig, ax = plt.subplots()
    ax.scatter(data[x_column], data[y_column], alpha=0.5)
    ax.set_title(f"{x_column} vs. {y_column}")
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    st.pyplot(fig)

st.write("Explore the dataset further by filtering or adding your custom visualizations!")
