# app.py

import streamlit as st
# import pandas as pd
import pickle

# Load the trained machine learning model
with open('xgb.pkl', 'rb') as model_file:
    model = pickle.load(model_file)


def main():
    st.title('Fraud Detection App')

    # Collect input features from the user
    claim_amount = st.number_input('Enter Claim Amount')
    claim_type = st.selectbox('Select Claim Type', ['Auto', 'Health', 'Property'])

    # When the user clicks the "Detect Fraud" button
    if st.button('Detect Fraud'):
        # Make a prediction using the loaded model
        prediction = model.predict([[claim_amount, claim_type]])

        # Display the prediction result
        st.subheader('Prediction Result:')
        if prediction[0] == 1:
            st.error('Fraud Detected!')
        else:
            st.success('No Fraud Detected.')


if __name__ == '__main__':
    main()
