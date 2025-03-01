import streamlit as st
import pandas as pd

st.title("My First Streamlit App")

st.write("Hello, world!")

# Allow only CSV and Excel files
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        # Read the file based on its extension
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a CSV or Excel file.")
            df = None
        
        # Display the dataframe if it was successfully read
        if df is not None:
            st.dataframe(df)
    except Exception as e:
        st.error(f"Error: {e}")