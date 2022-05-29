import json
import numpy as np
import pandas as pd
import requests
import sklearn
import streamlit as st
from streamlit_lottie import st_lottie
import pickle

from explore_page import show_explore_page
from Predict_page import show_predict_page

car=pd.read_csv('clean_car_set.csv')

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jrpzvtqz.json")
lottie_car1 = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_a3emlnqk.json")
lottie_thnxu = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_qn2snk.json")



def main():
    string = "Car Data Analysis"
    st.set_page_config(page_title=string, page_icon="🚗") 
    st.title("Car Data Analysis 🚗")
    st.markdown("### WELCOME ! Don't deny yourself the pleasure of driving the best premium cars from around the world here and now 🤖 ")
    
    st_lottie(lottie_coding)
    st_lottie(lottie_car1)
    


    page = st.sidebar.selectbox("Explore or Predict", ("Explore", "Predict"))
    
    if page == "Predict":
        show_predict_page()
        st_lottie(lottie_thnxu)  
    else:
        show_explore_page()   

  

if __name__ == '__main__':
    main()    


