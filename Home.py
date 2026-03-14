import streamlit as st
from user_authentication.user_authentication import authenticate

st.title("Welcome to My App")

tab1, tab2 = st.tabs(["Sign In", "Sign Up"])

with tab1:
    st.header("Login")
    email = st.text_input("Email Address", key="login_email")
    password = st.text_input("Password", type="password", key="login_pass")
    if st.button("Login"):
        if authenticate(email,password):
            print("User verified.......")
            st.success(f"Logging in {email}...")
        else:
            st.text("Authentication failed.......")
        

with tab2:
    st.header("Create Account")
    new_user = st.text_input("Username", key="reg_user")
    new_email = st.text_input("Email", key="reg_email")
    new_pass = st.text_input("Password", type="password", key="reg_pass")
    if st.button("Sign Up"):
        st.info("Account created! You can now sign in.")