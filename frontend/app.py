import streamlit as st
import predict
import login
import data

def display_welcome_message():
    st.title("Personality Prediction App")
    st.write("""
    Welcome to the Personality Prediction App!

    This web application uses the K-Nearest Neighbors (KNN) algorithm to predict personality types based on your responses. You can choose between two test lengths:

    - 60-Question Test: Provides a detailed analysis of your personality with higher accuracy.
    - 20-Question Test: Offers a quicker overview of your personality type but may have lower accuracy (accuracy may drop from 99% to around 92%).

    **Please log in or sign up to take the Free Personality Test.**
             
    Both tests classify you into one of 16 personality types. Here is a brief description of each type:
    """)

def initialize_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'page' not in st.session_state:
        st.session_state.page = "Home"
    if 'feedback_submitted' not in st.session_state:
        st.session_state.feedback_submitted = False
    if 'prediction_made' not in st.session_state:
        st.session_state.prediction_made = False

def display_sidebar():
    st.sidebar.title("Account")

    if not st.session_state.logged_in:
        if 'login' not in st.session_state:
            st.session_state.login = True  # Show login form by default

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.session_state.login:
                login_form()
            else:
                sign_up_form()
    else:
        st.sidebar.write(st.session_state.get('login_email', ''))
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.page = "Home"
            st.session_state.login_email = ""
            st.session_state.login_password = ""
            st.session_state.signup_password = ""

def display_home_page():
    st.subheader("Personality Types and Descriptions")
    for index, description in data.personality_types.items():
        st.markdown(f"""
            <div style="border-radius: 5px; background-color: #8B0000; padding: 10px; margin: 10px 0; color: #FFD700;">
                <strong>{index}:</strong> {description}
            </div>
            """, unsafe_allow_html=True)

def display_page():
    page = st.session_state.page

    if page == "Home":
        display_home_page()
    elif page == "Login":
        login.login()
    elif page == "Predict":
        if st.session_state.get("logged_in", False):
            predict.predict(data.questions, data.personality_types)
        else:
            st.warning("Please log in to access the prediction page.")

def login_form():
    st.sidebar.header("Log in")
    email = st.sidebar.text_input("Email address", key="login_email")
    password = st.sidebar.text_input("Password", type="password", key="login_password")

    if st.sidebar.button("Log in"):
        login.login_user(email, password)

    st.sidebar.write("")
    if st.sidebar.button("Create new account"):
        st.session_state.login = False

def sign_up_form():
    st.sidebar.header("Create new account")
    name = st.sidebar.text_input('First name')
    surname = st.sidebar.text_input('Surname')
    email = st.sidebar.text_input("Email", key="login_email")
    password = st.sidebar.text_input("Password", type="password", key="signup_password")
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

    if st.sidebar.button("Sign Up"):
        if email.endswith("@gmail.com"):
            login.create_user(name, surname, email, password, gender)
            initialize_session_state()
        else:
            st.sidebar.error("Please use a valid email address")

    st.sidebar.write("")
    if st.sidebar.button("Go back"):
        st.session_state.login = True


def main():
    display_welcome_message()
    initialize_session_state()
    display_sidebar()
    display_page()

if __name__ =="__main__":
    main()
