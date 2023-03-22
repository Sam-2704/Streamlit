import streamlit as st

# Set page title
st.set_page_config(page_title="Life Tracking App", page_icon=":bar_chart:")

# Define the app header
st.title("Welcome to the Life Tracking App!")
st.subheader("Track and improve your daily habits and routines.")

# Define the navigation menu
menu = ["Home", "Sleep Tracker", "Exercise Tracker", "Water Tracker"]
choice = st.sidebar.selectbox("Select an option", menu)

# Define the content for each menu option
if choice == "Home":
    st.write("Welcome to the Life Tracking App! Choose an option from the sidebar to get started.")
elif choice == "Sleep Tracker":
    # Define sleep tracking form here
    pass
elif choice == "Exercise Tracker":
    # Define exercise tracking form here
    pass
elif choice == "Water Tracker":
    # Define water tracking form here
    pass
