import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.compose import ColumnTransformer

# Reading two pickle models from pickle files
model_voting=pickle.load(open('voting_classifier.pkl','rb'))
col_transform=pickle.load(open('column_transformer.pkl','rb'))
model_regression=pickle.load(open('Random_forest_reg.pkl','rb'))

st.title("Student Campus Placement Prediction")

# Collecting user input
gender = st.selectbox("SSC Board", ["Male", "Female"])
ssc_p = st.number_input("SSC Percentage", 0, 100)
ssc_b = st.selectbox("SSC Board", ["Central", "Others"])
hsc_p = st.number_input("HSC Percentage", 0, 100)
hsc_b = st.selectbox("HSC Board", ["Central", "Others"])
hsc_s = st.selectbox("HSC Stream", ["Science", "Commerce", "Arts"])
degree_p = st.number_input("Degree Percentage", 0, 100)
degree_t = st.selectbox("Degree Type", ["Comm&Mgmt", "Sci&Tech", "others"])
workex = st.selectbox("Work Experience", ["Yes", "No"])
etest_p = st.number_input("Employability Test Percentage", 0, 100)
specialisation = st.selectbox("Specialisation", ["Mkt&HR", "Mkt&Fin"])
mba_p = st.number_input("MBA Percentage", 0, 100)

gender = 1 if gender == 'Male' else 0

if st.button("Predict"):
# Creating input DataFrame
    input_data = pd.DataFrame({
        'gender': [gender],
        'ssc_p': [ssc_p],
        'ssc_b': [ssc_b],
        'hsc_p': [hsc_p],
        'hsc_b': [hsc_b],
        'hsc_s': [hsc_s],
        'degree_p': [degree_p],
        'degree_t': [degree_t],
        'workex': [workex],
        'etest_p': [etest_p],
        'specialisation': [specialisation],
        'mba_p': [mba_p]
    })

    # transforming the input data using column transformer
    input_data_transformed=col_transform.transform(input_data)

    # predicting the output using the model
    y_pred=model_voting.predict(input_data_transformed)

    # Displaying the result
    # Displaying the result
    if y_pred == 1:  # If placed
        st.success("Placed. Congrats.")
        
        # Predicting salary for placed student using the regression model
        predicted_salary = model_regression.predict(input_data_transformed)
        st.success(f"The predicted salary for the student is: ${predicted_salary[0]:.2f}")
        
    else:
        st.error("Not Placed. Study Hard")
