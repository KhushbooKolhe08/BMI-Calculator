# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:36:01 2020

@author: asus
"""


import streamlit as st
from PIL import Image
st.title('Welcome to BMI Calculator')

#bmi image
img = Image.open("bmi.jpg")
st.image(img,width=200)

hmode=0

#weight
weight = st.number_input("Enter your weight in kgs")
#height
status = st.radio("Enter your height format", ('cm','meters','feet'))
if(status == 'cm'):
    h_mode = 0
    height = st.number_input('Centimeters')
elif(status == 'meters'):
    h_mode = 1
    height = st.number_input('Meters')
else:
    h_mode = 2
    height = st.number_input('Feet')   

if(st.button('Calculate BMI')):
    if(h_mode == 0):
        bmi = weight / ((height/100)**2)
        st.text(bmi)
        
    elif(h_mode == 1):
        bmi = weight / (height ** 2)
        st.text(bmi)
    else:
        # 1 meter = 3.28
        bmi = weight / (((height/3.28))**2)
        st.text(bmi)
           
    print('-----------------------------------------------------------------')
    if(bmi < 16):
        st.error("You are Extremly Underweight")
    elif(bmi >=16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >=18.5 and bmi < 25):
        st.success("You are Totally Healthy")
        st.balloons()
    elif(bmi > 25):
       st.error("You are Extremly Underweight")
    print('-----------------------------------------------------------------')        
                  