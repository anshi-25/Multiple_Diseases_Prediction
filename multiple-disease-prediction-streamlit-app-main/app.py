# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:52:13 2024

@author: ayush
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# load the models_saved

diabetes_model = pickle.load(open('C:/Users/ayush/Documents/Multiple_Disease_Prediction/multiple-disease-prediction-streamlit-app-main/Model_saved/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/ayush/Documents/Multiple_Disease_Prediction/multiple-disease-prediction-streamlit-app-main/Model_saved/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('C:/Users/ayush/Documents/Multiple_Disease_Prediction/multiple-disease-prediction-streamlit-app-main/Model_saved/parkinsons_model.sav', 'rb'))

breastcancer_disease_model = pickle.load(open('C:/Users/ayush/Documents/Multiple_Disease_Prediction/multiple-disease-prediction-streamlit-app-main/Model_saved/breastcancer_disease_model.sav', 'rb'))



with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Breast Cancer Prediction',
                            'Parkinsons Prediction'],
                           
                           icons=['activity','heart','activity','person'],
                           default_index=0)
    
# for diabetes disease prediction    
    
if (selected == 'Diabetes Prediction'):

    st.title('Diabetes Disease Prediction')
    
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

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
            
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)
    
 #for heart disease prediction
    
if (selected == 'Heart Disease Prediction'):

    st.title('Heart Disease Prediction') 
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''


    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
            
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    
# for parkinsons disease prediction    
    
if (selected == 'Parkinsons Prediction'):

    st.title('Parkinsons Disease Prediction') 

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''
    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
            
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

# for breast cancer disease prediction    
    
if (selected == 'Breast Cancer Prediction'):

    st.title('Breast Cancer Disease Prediction') 

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        id = st.text_input('Unique ID')

    with col2:
       radius_mean = st.text_input('Radius of Lobes')

    with col3:
       texture_mean = st.text_input('Mean of Surface Texture')

    with col4:
        perimeter_mean = st.text_input('Outer Perimeter of Lobes')

    with col5:
        area_mean = st.text_input('Mean Area of Lobes')

    with col1:
        smoothness_mean = st.text_input('Mean of Smoothness Levels')

    with col2:
       compactness_mean = st.text_input('Mean of Compactness')

    with col3:
        concavity_mean = st.text_input('Mean of Concavity')

    with col4:
        concave_points_mean = st.text_input('Mean of Cocave Points')

    with col5:
        symmetry_mean = st.text_input('Mean of Symmetry')

    with col1:
        fractal_dimension_mean = st.text_input('Mean of Fractal Dimension')

    with col2:
        radius_se = st.text_input('SE of Radius')

    with col3:
        texture_se = st.text_input('SE of Texture')

    with col4:
        perimeter_se = st.text_input('Perimeter of SE')

    with col5:
        area_se = st.text_input('Are of SE')

    with col1:
        smoothness_se = st.text_input('SE of Smoothness')

    with col2:
        compactness_se = st.text_input('SE of compactness')

    with col3:
        concavity_se = st.text_input('SEE of concavity')

    with col4:
        concave_points_se = st.text_input('SE of concave points')

    with col5:
        symmetry_se = st.text_input('SE of symmetry')

    with col1:
        fractal_dimension_se = st.text_input('SE of Fractal Dimension')

    with col2:
        radius_worst = st.text_input('Worst Radius')

    with col3:
        texture_worst = st.text_input('Worst Texture')

    with col4:
        perimeter_worst = st.text_input('Worst Permimeter')

    with col5:
        area_worst = st.text_input('Worst Area')
        
    with col1:
       smoothness_worst = st.text_input('Worst Smoothness')

    with col2:
        compactness_worst = st.text_input('Worse Compactness')

    with col3:
       concavity_worst = st.text_input('Worst Concavity')

    with col4:
        concave_points_worst = st.text_input('Worst Concave Points')

    with col5:
        symmetry_worst = st.text_input('Worst Symmetry') 
        
    with col1:
         fractal_dimension_worst = st.text_input('Worst Fractal Dimension')

    with col2:
         diagnosis_encoded = st.text_input('Target: 1 - Malignant 0 - Benign')   

    # code for Prediction
    breastcancer_diagnosis = ''
    
    if st.button("Breast Cancer Test Result"):

        user_input = [id,radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst,diagnosis_encoded]

        user_input = [float(x) for x in user_input]

        breastcancer_prediction = breastcancer_disease_model.predict([user_input])

        if (breastcancer_prediction[0] == 1):
            breastcancer_diagnosis = "The Breast Cancer is Malignant"
            
        else:
            breastcancer_diagnosis = "The Breast Cancer is Benign"

    st.success(breastcancer_diagnosis)    
    
    
    