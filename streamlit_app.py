import streamlit as st

# Title for the GUI
st.title("Simple Streamlit App")

# Button interaction
if st.button("Click Me!"):
    st.success("Button Clicked!")

# Display a message
st.write("Welcome to the simple Streamlit GUI!")
