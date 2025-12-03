#!pip install streamlit
import streamlit as st
import pandas as pd
from joblib import load
from sklearn.preprocessing import LabelEncoder

model =load('heart_failure_prediction.joblib')


st.title('Heart Failure Prediction App')

st.header('Enter Patient Details') 
age = st.number_input('Age',min_value=1,max_value=120,step=1)
anaemia = st.selectbox('Anaemia (0=No,1=Yes)',[0,1])
creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase", min_value=0, step=1)
diabetes = st.selectbox('Diabetes(0=No,1=Yes)', [0, 1])
ejection_fraction = st.number_input("Ejection Fraction (%)", min_value=1, max_value=100, step=1)
high_blood_pressure = st.selectbox('High Blood Pressure (0 =No, 1 =Yes)', [0, 1])
platelets = st.number_input("Platelets", min_value=0, step=1)
serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", min_value=0.0)
serum_sodium = st.number_input("Serum Sodium (mEq/L)", min_value=100, max_value=200)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
smoking = st.selectbox("Smoking (0 = No, 1 = Yes)", [0, 1])
time = st.number_input("Follow-up Period (days)", min_value=1, step=1)






input_data = pd.DataFrame({
    'age': [age],
    'anaemia': [anaemia],
    'creatinine_phosphokinase': [creatinine_phosphokinase],
    'diabetes': [diabetes],
    'ejection_fraction': [ejection_fraction],
    'high_blood_pressure': [high_blood_pressure],
    'platelets': [platelets],
    'serum_creatinine': [serum_creatinine],
    'serum_sodium': [serum_sodium],
    'sex': [sex],
    'smoking': [smoking],
    'time': [time]
})



if st.button("Predict"):
    model = load('heart_failure_prediction.joblib')

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠ High Risk of Death")
    else:
        st.success("✔ Low Risk of Death")

