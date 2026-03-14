import streamlit as st

user_name = st.text_input(label='user_name')

user_password = st.text_input(label='user_password')

print(user_name, user_password)