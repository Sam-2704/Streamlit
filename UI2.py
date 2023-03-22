import streamlit as st

st.set_page_config(page_title="Life Tracking App", page_icon=":chart_with_upwards_trend:")

# Sidebar
st.sidebar.title("Menu")
page = st.sidebar.selectbox("Select a page", ["Home", "Fitness", "Sleep", "Meditation"])

# Home page
if page == "Home":
    st.title("Welcome to the Life Tracking App!")
    st.write("Track your daily activities and habits to improve your life.")
    st.write("")
    st.subheader("Quick Log")
    activity = st.text_input("Activity")
    duration = st.slider("Duration (in minutes)", 0, 120, 30)
    log_button = st.button("Log")
    if log_button:
        st.success(f"Logged {activity} for {duration} minutes.")
    
# Fitness page
elif page == "Fitness":
    st.title("Fitness Tracker")
    st.write("Log your workouts and track your progress.")
    st.write("")
    st.subheader("Quick Log")
    workout = st.selectbox("Workout", ["Running", "Cycling", "Swimming"])
    distance = st.slider("Distance (in km)", 0.0, 10.0, 5.0)
    time = st.slider("Time (in minutes)", 0, 120, 30)
    log_button = st.button("Log")
    if log_button:
        st.success(f"Logged {distance} km {workout} in {time} minutes.")
        
# Sleep page
elif page == "Sleep":
    st.title("Sleep Tracker")
    st.write("Log your sleep and track your patterns.")
    st.write("")
    st.subheader("Quick Log")
    sleep_start = st.time_input("Start time")
    sleep_end = st.time_input("End time")
    log_button = st.button("Log")
    if log_button:
        st.success(f"Logged sleep from {sleep_start} to {sleep_end}.")
        
# Meditation page
elif page == "Meditation":
    st.title("Meditation Tracker")
    st.write("Log your meditation sessions and track your progress.")
    st.write("")
    st.subheader("Quick Log")
    duration = st.slider("Duration (in minutes)", 0, 60, 10)
    log_button = st.button("Log")
    if log_button:
        st.success(f"Logged {duration} minutes of meditation.")
