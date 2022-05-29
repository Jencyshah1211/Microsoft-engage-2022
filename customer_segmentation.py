import numpy as np
import pandas as pd
import streamlit as st
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import pandas.util.testing as tn
car = pd.read_csv('clean_car_set.csv')
sns.set_style('darkgrid')
def show_segmentation():

  encodedOutput_y = LabelEncoder()
  car['Make']= encodedOutput_y.fit_transform(car.iloc[:,1].values)
  Z = car[['Ex-Showroom_Price','Make']].values
  from sklearn.cluster import KMeans
  wcss=[]
  for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init="k-means++",random_state=42)
    kmeans.fit(Z)
    wcss.append(kmeans.inertia_)

  sns.set()
  data = (range(1,11),wcss)
   
  kmeans = KMeans(n_clusters=3, init='k-means++', random_state=0)
  Cluster_label = kmeans.fit_predict(Z)
  
  fig = plt.figure(figsize=(10,4))
  plt.scatter(x = Z[Cluster_label==0,0],y = Z[Cluster_label==0,1], label = 'Customer1')
  plt.scatter(x = Z[Cluster_label==1,0],y =  Z[Cluster_label==1,1],label = 'Customer2')
  plt.scatter(x = Z[Cluster_label==2,0],y = Z[Cluster_label==2,1], label = 'Customer3')
  plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],label="Centroids")
  st.balloons()
  st.pyplot(fig)
  
  
  st.write("""### We have got 3 clusters of customers 1) The blue colour dots represents that major number of cars are of low budget and that is designed for people with low inome.Hence, it shows people which are having low income. 2) The green colour dots represents the number of cars which are having medium price range. They are designed for people with medium income. Hence, it shows people with medium budget 3) The orange colour dots shows cars with high price range. They are designed for people having high income.Hence, it shows people with high budget.""")