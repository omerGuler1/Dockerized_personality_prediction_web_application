import streamlit as st
import requests

url = "http://backend:8000"

def create_user(name, surname, email, password, gender):
    response = requests.post(f"{url}/users/", json={
        "name": name,
        "surname": surname,
        "email": email,
        "password": password,
        "gender": gender
    })
    if response.status_code == 201 or response.status_code == 200:
        st.sidebar.success("Registered successful")
        st.session_state.logged_in = True
        st.session_state.page = "Predict"
        st.session_state.feedback_submitted = False
    else:
        st.sidebar.error("Registration failed")
    return response.json()

def login_user(email, password):
    response = requests.post(f"{url}/login/", json={"email": email, "password": password})
    if response.status_code == 200:
        st.sidebar.success("Login successful")
        st.session_state.logged_in = True
        st.session_state.page = "Predict"
        st.session_state.feedback_submitted = False
    else:
        error_message = response.json().get("detail", "Login failed")
        if "username" in error_message.lower():
            st.sidebar.error("Invalid username")
        elif "password" in error_message.lower():
            st.sidebar.error("Invalid password")
        else:
            st.sidebar.error("Login failed")
