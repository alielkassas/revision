import streamlit as st
import functions

st.title("My dummy app")

clicked = st.button("Inspire Me")
if clicked:
	st.ballons()
    
    