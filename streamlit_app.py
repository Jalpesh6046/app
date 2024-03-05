
import streamlit as st
import requests

# Define your API endpoint
API_ENDPOINT = "https://app-gzqz.onrender.com/"

def predict_output(index, experience, test_score, api_key):
    index = float(index)
    experience = float(experience)
    test_score = float(test_score)

    # Make a POST request to the API endpoint with the payload and API key
    payload = {
        "Index": index,
        "experience": experience,
        "test_score": test_score
    }
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.post(API_ENDPOINT, json=payload, headers=headers)

    # Check if the request was successful and return the prediction
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        return prediction
    else:
        st.error("Failed to get prediction from the API")
        return None

def main():
    st.title("Salary Prediction App")

    # User input for API key
    api_key = st.text_input("Enter your API key:", type="password")

    # User input for salary prediction
    index = st.text_input("Index*")
    experience = st.text_input("Number of years experience*")
    test_score = st.text_input("Test score*")

    # Perform prediction when the user clicks the button
    if st.button("Predict"):
        if index and experience and test_score and api_key:
            result = predict_output(index, experience, test_score, api_key)
            if result is not None:
                st.success("Predicted Salary: ${:.2f}".format(result))
        else:
            st.error("Please fill in all the required fields including the API key.")

if __name__ == "__main__":
    main()
