import streamlit as st
import requests

def feedback():
    # Collect feedback from the user
    feedback = st.radio("Is this prediction accurate?", ("Yes", "No"))

    feedback_payload = {
        'feedback': feedback,
        'prediction': st.session_state.predicted_value
    }

    # Use a form to handle feedback submission
    with st.form(key='feedback_form'):
        submit_button = st.form_submit_button('Submit Feedback')
        if submit_button:
            feedback_response = requests.post('http://backend:8000/feedback', json=feedback_payload)
            st.session_state.feedback_submitted = True

    if st.session_state.feedback_submitted:
        if feedback_response.status_code == 200:
            st.write("Thank you for your feedback!")
            st.session_state.feedback_submitted = False
        else:
            st.write(f"Error: {feedback_response.status_code} - {feedback_response.text}")

def make_prediction(question_values, personality_types):
    st.session_state.feedback_submitted = False

    input_data = {
        **question_values
        }

    # Send a single dictionary instead of a DataFrame
    request_payload = {
        'input_data': input_data,
        }

        
    # response = requests.post('http://localhost:8000/predict', json=request_payload)
    response = requests.post('http://backend:8000/predict', json=request_payload)

    if response.status_code == 200:
        result = response.json()

        if 'predicted_personality' in result:
            predicted_value = result['predicted_personality']

            # Ensure predicted_value is an integer
            if isinstance(predicted_value, int):
                personality_description = personality_types.get(predicted_value, "Unknown Personality Type (default)")
                st.write(f'Predicted Personality: {personality_description}')
            else:
                st.write("Unexpected predicted value type.")
                st.write(result)
                
            # Indicate that a prediction has been made
            st.session_state.prediction_made = True
            st.session_state.predicted_value = predicted_value

        else:
            st.write(f"Unexpected response: {result}")
    else:
        st.write(f"Error: {response.status_code} - {response.text}")

    
def predict(questions, personality_types):

    st.title('Personality Prediction')

    num_questions = st.radio('Number of Questions', options=[20, 60], index=1)


    question_values = {}
    for i in range(1, num_questions + 1):
        question_values[f'q{i}'] = st.number_input(f'Q{i}: {questions[i-1]}', min_value=-3, max_value=3, value=0)


    if st.button('Predict'):
        make_prediction(question_values, personality_types)
    if st.session_state.prediction_made:
        feedback()