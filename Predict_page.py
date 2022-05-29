import streamlit as st
import pandas as pd
import json
import requests
from streamlit_lottie import st_lottie
import numpy as np
import sklearn
import pickle
    
car = pd.read_csv('clean_car_set.csv')

with open('LR_price_model.pkl', 'rb') as f:
  model = pickle.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_price = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_49rdyysj.json")

def show_predict_page():

 st.write("""### Welcome to Price Prediction Page""")
 st_lottie(lottie_price)
 st.balloons()
 company = car['Make'].unique()
 car_model = car['Model'].unique()
 variant = car['Variant']
 fuel_type = car['Fuel_Type'].unique()
 select_company = st.selectbox("Select Company name ", company)
 
 select_Model = st.selectbox("Select Model ", car_model)
 
 select_variant = st.selectbox("Select variant ", variant)
 
 select_fuel_type = st.selectbox("Select Fuel Type ", fuel_type)
 
 st.write(' ')
 if st.button("Estimate Price", key='predict'):
    try:
            
            prediction = model.predict(pd.DataFrame([[select_company, select_Model, select_variant, select_fuel_type]],columns=['Make','Model','Variant','Fuel_Type']))
            output = round(prediction[0],5)
            if output<0:
                st.warning("Please select correct model and variant ")
            else:
                st.success("The predicted Price of your car is {} lakhs 🙌".format(output))
    except:
            st.warning("Opps!! Something went wrong\nTry again")
