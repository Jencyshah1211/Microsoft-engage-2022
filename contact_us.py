import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_contact = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_vrcurbxk.json")

def show_contact_page():
    st_lottie(lottie_contact) 




