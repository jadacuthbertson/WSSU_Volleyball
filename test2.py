import streamlit as st
import pandas as pd

# Load some sample data
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Create a select box for the x-axis
x_column = st.selectbox("Choose a column for the x-axis", df.columns)

# Plot the scatter chart using the selected column
st.scatter_chart(data=df, x=x_column)