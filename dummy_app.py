import streamlit as st

st.title("My dummy app")

clicked = st.button("Inspire Me")
if clicked:
	st.balloons()
