import streamlit as st

myname = st.text_input('name :')

if st.button('Search'):
    st.write(f"search name : {myname}")