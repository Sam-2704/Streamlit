# Import the required libraries
import streamlit as st
from datetime import datetime

# Define the title of the app
st.title("My Life Tracking Home Page")

# Add a sidebar with navigation options
menu = ["Home", "Workout", "Nutrition", "Sleep"]
choice = st.sidebar.selectbox("Select a page", menu)

# Create a function to get the current date and time
def get_time():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")

# Define the home page content
if choice == "Home":
    st.subheader("Welcome to my life tracking home page!")
    st.write("Here, you can track various aspects of your life and keep a record of your progress.")
    st.write("To get started, select a page from the sidebar.")
    
# Define the workout page content
elif choice == "Workout":
    st.subheader("Workout Tracking")
    exercise = st.text_input("Enter your exercise")
    weight = st.number_input("Enter your weight (lbs)", min_value=0, step=1)
    sets = st.number_input("Enter number of sets", min_value=0, step=1)
    reps = st.number_input("Enter number of reps", min_value=0, step=1)
    time = get_time()
    if st.button("Add workout"):
        st.write(f"{time} - {exercise}: {sets} sets of {reps} reps at {weight} lbs")
    
# Define the nutrition page content
elif choice == "Nutrition":
    st.subheader("Nutrition Tracking")
    food = st.text_input("Enter the food you ate")
    calories = st.number_input("Enter the number of calories", min_value=0, step=1)
    time = get_time()
    if st.button("Add food"):
        st.write(f"{time} - {food}: {calories} calories")
    
# Define the sleep page content
elif choice == "Sleep":
    st.subheader("Sleep Tracking")
    hours = st.number_input("Enter the number of hours of sleep", min_value=0, step=0.25)
    time = get_time()
    if st.button("Add sleep"):
        st.write("f{time} - {hours} hours of sleep")
        
