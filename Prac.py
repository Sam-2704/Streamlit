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
      st.subheader("Sleep Tracking")
    hours = st.number_input("Enter the number of hours of sleep", min_value=0, step=1)
    time = get_time()
    if st.button("Add sleep"):
        st.write("f{time} - {hours} hours of sleep")
        
elif choice == "Exercise Tracker":
    st.subheader("Exercise Tracker")
    exercise = st.text_input("Enter your exercise")
    weight = st.number_input("Enter your weight (lbs)", min_value=0, step=1)
    sets = st.number_input("Enter number of sets", min_value=0, step=1)
    reps = st.number_input("Enter number of reps", min_value=0, step=1)
    time = get_time()
    if st.button("Add workout"):
        st.write(f"{time} - {exercise}: {sets} sets of {reps} reps at {weight} lbs")
elif choice == "Water Tracker":
    # Define water tracking form here
    pass
