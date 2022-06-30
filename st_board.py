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


st.header('Dashboard for Bank Identification') 



choice_db = st.sidebar.selectbox(
        'Données connues ou entrer données ? ',
        ['Dataset','imposer'])
st.sidebar.write('Welcome to Bank Authotentification Prediction')

st.sidebar.image: st.sidebar.image("images.jpg", use_column_width=True)
st.sidebar.write('Description, *World!* :sunglasses: :')
st.sidebar.write('This app is made for an example of using Streamlit and request an api made for prediction, and hosted on Heroku. ')
st.sidebar.write('Done Michel Blazevic: https://github.com/Mich-Blaz')

#CHOIX si on fait un choix à la main ou dans la base de données: 
var1,var2,var3,var4 = st.columns(4)

if choice_db=='imposer': 
    variance = var1.number_input('valeur pour la variance',
                                 min_value=df.variance.min()-1, value=df.variance.mean(), step=0.1)

    skewness = var2.number_input('valeur pour skewness',
                              min_value=df.skewness.min()-1, value=df.skewness.mean(), step=0.1)

    curtosis = var3.number_input('Valeur curtosis',
                                   min_value=df.curtosis.min()-1, value=df.curtosis.mean(), step=0.1)

    entropy = var4.number_input('Valeur Entropy',
                                     min_value=df.curtosis.min()-1, value=df.curtosis.mean(), step=0.1)
    dic_id={"variance":variance,"skewness":skewness,"curtosis":curtosis,"entropy":entropy}
#Select index 
else:

    id_bk = st.selectbox("Select_index", pd.unique(df.index))
    dic_id=df.loc[id_bk,df.columns[:-1]].to_dict()


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


res=pd.Series(requests.post('https://michblazfastapi.herokuapp.com/predict',json=dic_id).json())

cont1,cont2=st.columns(2)
cont1.metric(label=res.prediction,
             value=res.predd,
		delta=res.pred_proba)



labels=['True Bank Auth','False Bank Auth']
sizes=[1-res.pred_proba,res.pred_proba]

fig, ax = plt.subplots(figsize=(2,2))
ax.pie(sizes,  labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=0)
ax.axis('equal')
cont2.pyplot(fig)

st.write("*Body à envoyer dans la requête http de l'api de pred:*   \n" +str(dic_id))

# variance,skewness,curtosis,entropy,class

col1, col2 = st.columns(2)
fig, ax = plt.subplots(figsize=(10,10))
sns.scatterplot(data=df,x="variance",y="skewness",hue="class",ax=ax)

col1.pyplot(fig)

fig, ax = plt.subplots(figsize=(10,10))
sns.scatterplot(data=df,x="curtosis",y="skewness",hue="class",ax=ax)

col2.pyplot(fig)

#Sidebar


