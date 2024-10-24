import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

    # page title
st.title('Detecting Diabetes using Random Forest By The Power Of Feature Engineering')

# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Pregnancies = st.text_input('Number of Pregnancies')

with col2:
    Glucose = st.text_input('Glucose Level')

with col3:
    BloodPressure = st.text_input('Blood Pressure value')

with col1:
    SkinThickness = st.text_input('Skin Thickness value')

with col2:
    Insulin = st.text_input('Insulin Level')

with col3:
    BMI = st.text_input('BMI value')

with col1:
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

with col2:
    Age = st.text_input('Age of the Person')


# code for Prediction
diab_diagnosis = ''

# creating a button for Prediction

if st.button('Diabetes Test Result'):

    user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                    BMI, DiabetesPedigreeFunction, Age]

    user_input = [float(x) for x in user_input]

    diab_prediction = diabetes_model.predict([user_input])

    if diab_prediction[0] == 1:
        diab_diagnosis = 'Result: Oops! You have diabetes. We prescribe you medication such as metformin or insulin to help manage blood sugar levels Additionally, you are recommended to change your lifestyle including diet modifications and regular exercise to improve overall health and to better control the condition'
    else:
        diab_diagnosis = "Result: Great! You don't have diabetes. Maintain a balanced diet and regular exercise routine to promote overall health and prevent future health complications. Additionally, you are recommended to do regular check-ups to monitor blood sugar levels and overall health status."

st.success(diab_diagnosis)
