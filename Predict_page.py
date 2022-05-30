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
  LR_model = pickle.load(f)

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
 #Select company and model
 make = st.selectbox('Choose your company name' , car["Make"].unique())
 company_data = car[['Model' , 'Variant' , 'Fuel_Type' ,'Ex-Showroom_Price']].where(car['Make'] == make).dropna();
 model = st.selectbox('Choose your car name' , company_data["Model"].unique())
 variant_data = company_data[['Variant' , 'Fuel_Type', 'Ex-Showroom_Price']].where(company_data['Model'] == model).dropna();

 #Select variant
 variant = st.selectbox('Choose your variant name' , variant_data['Variant'].unique())

 #Select fuel type
 fuel_type = st.selectbox('Choose your Fuel_type ' , variant_data['Fuel_Type'].unique())
 if st.button("Estimate Price", key='predict'):
    try:
            
            prediction = LR_model.predict(pd.DataFrame([[make, model, variant, fuel_type]],columns=['Make','Model','Variant','Fuel_Type']))
            output = prediction
            if output<0:
                st.warning("Please select correct model and variant ")
            else:
                st.success("The predicted Price of your car is {} lakhs 🙌".format(output))
    except:
            st.warning("Opps!! Something went wrong\nTry again")
