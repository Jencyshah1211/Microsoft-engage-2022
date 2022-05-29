import json
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from customer_segmentation import show_segmentation
car = pd.read_csv('clean_car_set.csv')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_car2 = load_lottieurl("https://assets2.lottiefiles.com/datafiles/HN7OcWNnoqje6iXIiZdWzKxvLIbfeCGTmvXmEm1h/data.json")
lottie_bar = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_kwjwqk59.json")
lottie_pie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_btch1odn.json")
lottie_segment = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_xqbchnql.json")
lottie_thnx = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_sqpjokxl.json")
def show_explore_page():

    st.title("Explore page of Car dataset")
    st.markdown("""#### WELCOME to the Explore Page 🤖 """)
    st_lottie(lottie_car2)
    st.write("""### 1] Customer Segmentation """)
    st_lottie(lottie_segment)
    show_segmentation()
    st.write(" ")
    st.write("""#### 2] Legal and Illegal Cars """)
    st_lottie(lottie_pie)
    fig1, ax1 = plt.subplots()
    ax1.pie((car['Emission_Norm'].value_counts()),labels=(car['Emission_Norm'].value_counts().keys()),autopct = '%0.1f%%')
    ax1.axis("Equal")
    st.write("""#### Number of Cars with emission norms of BS6 BS3 and BS4""")
    st.pyplot(fig1)
    st.write("""#### This shows that most of the cars belong to BS4 and the cars belonging to emission norm less than BS6 are illegal. Hence these cars need to launch their new updated versions. """)
    st.write(" ")

    st.write("""### 3] Bar plot based on Body Type""")
    st_lottie(lottie_bar)
    st.bar_chart(car['Body_Type'].value_counts())
    st.write("""### This shows that suv, Hatchback and sedan are major body type""")
    st.write(" ")

    st.write(" ")
    st.write("""### 4] Heatmap """)
    corr = car.corr()
    fig = plt.figure(figsize=(20,10))
    a = sns.heatmap(corr,annot=True,fmt='.2f', cmap = sns.diverging_palette(20, 220, n=200))
    st.pyplot(fig)
    st.write("""### It shows that Kerb-weight is positively corelated and city-mileage and highway-mileage are negatively corelated.""")
    st.write(" ")
    
    st.write(" ")
    st.write("""### 5] Mix graph """)
    g = sns.pairplot(car[["City_Mileage","Kerb_Weight","Drivetrain","Fuel_Type","Ex-Showroom_Price"]],hue="Fuel_Type", diag_kind="hist")
    st.pyplot(g)
    st.write("""### Findings: 1)Vehicle mileage decreases as kerb-weight increases. 2)kerb-weight is positively corelated with price.""")

    st.write(" ")
    st.write("""### 6] Box-plot """)
    fig = plt.figure(figsize=(10,7))
    sns.boxplot(x="Drivetrain", y="Ex-Showroom_Price",data=car)
    st.pyplot(fig)
    st.write("""### Findings: All wheel drive are expensive followed by 4WD and RWD""")
    st.write(" ")

    st_lottie(lottie_thnx)

