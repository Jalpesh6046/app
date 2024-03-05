import os
import pickle
import streamlit as st
import pandas as pd
import numpy as np
api_key = os.getenv("API_KEY")

if not api_key:
    st.error("API key not found. Please set the `API_KEY` environment variable.")
    st.stop()  # Halt app execution if no API key is found
def main():
    html_temp = """
    <div style ="background-color: skyblue; padding: 1px">
    <h2 style ="color: black; text-align:center;">Salary Prediction </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("&nbsp;")

    # Input field for API key
    entered_api_key = st.text_input("API Key")

    if entered_api_key.strip() == api_key:  # Check key validity after trimming whitespace
        Index = st.text_input("Index*")
        experience = st.text_input("Number of years experience*")
        test_score = st.text_input("test_score*")

        if st.button("Predict"):
            if Index and experience and test_score:
                result = predict_output(Index, experience, test_score)
                st.success("Predicted Salary: ${:.2f}".format(result[0]))
            else:
                st.error("Please fill in all the required fields.")
    else:
        st.error("Invalid API key. Please enter the correct key to proceed.")
