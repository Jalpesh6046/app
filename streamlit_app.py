import streamlit as st
import pickle

# Define your API key
VALID_API_KEY = "VeILepxvmjA4Mc1eIUXmFAeaWZHc0Urt"

# Load your machine learning model
pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

def predict_output(Index, experience, test_score):
    
    Index = float(Index)
    experience = float(experience)
    test_score = float(test_score)
    
    prediction = model.predict([[Index, experience, test_score]])
    
    return prediction

def main():
    # Display a form for users to enter their API key
    api_key = st.text_input("Enter your API Key:")

    # Check if the provided API key matches the valid API key
    if api_key.strip() == "":
        st.warning("Please enter your API Key.")
    elif api_key == VALID_API_KEY:
        # Display the salary prediction form if the API key is valid
        html_temp = """
        <div style ="background-color: skyblue; padding: 1px">
        <h2 style ="color: black; text-align:center;">Salary Prediction</h2>
        </div>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        st.write("&nbsp;")
        
        Index = st.text_input("Index*")
        experience = st.text_input("Number of years experience*")
        test_score = st.text_input("Test score*")
        
        if st.button("Predict"):
            if Index and experience and test_score:
                result = predict_output(Index, experience, test_score)
                st.success("Predicted Salary: ${:.2f}".format(result[0]))
            else:
                st.error("Please fill in all the required fields.")
    elif api_key != VALID_API_KEY:
        st.error("Invalid API Key. Access denied!")

if __name__ == "__main__":
    main()
