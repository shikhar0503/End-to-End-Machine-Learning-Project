import streamlit as st
import pickle
import sklearn
model = pickle.load(open('model.pkl', 'rb'))


#Creating GUI

st.title("Diabetes Prediction Web Application")
name = st.text_input("Name:")
pregnancy = st.number_input("Enter Number of pregnancy:")
glucose = st.number_input("Plasma Glucose Concentration:")
bp = st.number_input("Blood pressure (in mm Hg):")
skin = st.number_input("Triceps skin fold thickness (in mm):")
insulin = st.number_input("2-Hour serum insulin: ")
bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):")
dpf = st.number_input("Family History of Diabetes (0 = no, 1 = yes):")
age = st.number_input("Age:")
submit = st.button('Press to Predict')

if submit:
    prediction = model.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
    if prediction == 0:
        st.header("Congratulations {} you do not have a risk of being diabetic at present.".format(name))
    else:
        st.header("Sorry {} you have a risk of being diabetic. Please consult the doctor as soon as possible".format(name))