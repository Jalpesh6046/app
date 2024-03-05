import pickle
import streamlit as st
import pandas as pd
import numpy as np 


pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

def predict_output(Index, experience, test_score):
    
    Index = float(Index)
    experience = float(experience)
    test_score = float(test_score)
    
    prediction = model.predict([[Index, experience, test_score]])
    
    return prediction

def main():
    html_temp = """
<div style ="background-color: skyblue; padding: 1px">
<h2 style ="color: black; text-align:center;">Salary Prediction </h2>
</div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("&nbsp;")
    
    Index= st.text_input("Index*")
    experience= st.text_input("Number of years experience*")
    test_score=st.text_input("test_score*")
    
    if st.button("Predict"):

        if Index and experience and test_score:

            result = predict_output(Index, experience, test_score)
            st.success("Predicted Salary: ${:.2f}".format(result[0]))
        else:
            st.error("Please fill in all the required fields.")


if __name__ == "__main__":
    main()
    
