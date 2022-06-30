import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("BankNote_Authentication.csv")

st.set_page_config(
    page_title="Bank Authen pred",
    page_icon="✅",
    layout="wide",
)
#Select index 
id_bk = st.selectbox("Select_index", pd.unique(df.index))
dic_id=df.loc[id_bk].to_dict()

var1,var2,var3,var4 = st.columns(4)

var1.metric(
    label=df.columns[0],
    value=df.loc[id_bk,df.columns[0]],
    
)

var2.metric(
    label=df.columns[1],
    value=df.loc[id_bk,df.columns[1]],
    
)

var3.metric(
    label=df.columns[2],
    value=df.loc[id_bk,df.columns[2]],
    
)
var4.metric(
    label=df.columns[3],
    value=df.loc[id_bk,df.columns[3]],
    
)

st.write(str(dic_id))

# variance,skewness,curtosis,entropy,class
st.header('Dashboard for Bank Identification') 

col1, col2 = st.columns(2)
fig, ax = plt.subplots(figsize=(2,2))
sns.scatterplot(data=df,x="variance",y="skewness",hue="class",ax=ax)

col1.pyplot(fig)

fig, ax = plt.subplots(figsize=(4,4))
sns.scatterplot(data=df,x="curtosis",y="skewness",hue="class",ax=ax)

col2.pyplot(fig)

#Sidebar
st.sidebar.write('Welcome to Bank Authotentification Prediction')

st.sidebar.image: st.sidebar.image("images.jpg", use_column_width=True)
st.sidebar.write('Description, *World!* :sunglasses: :')
st.sidebar.write('This app is made for an example of using Streamlit and request an api made for prediction, and hosted on Heroku. ')



