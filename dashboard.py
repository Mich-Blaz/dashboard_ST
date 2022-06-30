import requests
import pandas as pd

bod=pd.Series({"variance":0,"skewness":0,"curtosis":0,"entropy":0})


r=pd.Series(requests.post('https://michblazfastapi.herokuapp.com/predict',json=bod.to_dict()).json())


for key in r.index:
    print(key,'valeur:',r[key],'type',type(r[key]))




import streamlit as st

st.sidewrite("some text")


