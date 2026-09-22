import streamlit as st
import functions

st.title("My dummy app")
rec_df =  functions.load_data('recipe.csv')

clicked = st.button("Inspire Me")
if clicked:
    random = functions.show_random(rec_df)
    st.write(random)
    
    