# Import the required libraries
import streamlit as st

# Define the title of the app
st.title("My Streamlit App")

# Add some text to the app
st.write("Welcome to my Streamlit app! Here, we'll explore the Streamlit library.")

# Add a slider to the app
age = st.slider("Select your age", 0, 100, 25)

# Add a selectbox to the app
gender = st.selectbox("Select your gender", ("Male", "Female", "Other"))

# Add a checkbox to the app
agree = st.checkbox("I agree to the terms and conditions")

# Add a button to the app
if st.button("Submit"):
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Agreed to terms and conditions:", agree)
