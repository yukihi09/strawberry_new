import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import base64
import csv
import os
import openpyxl
import random
from PIL import Image

st.title('イチゴの官能評価')
st.header('新規の画像を既存の順位の中に入れ込む')
st.write('左のイチゴの熟度はどの間に入りますか') # markdown


df = pd.read_csv('result.csv',encoding='cp932')
lst_image = df.values.tolist()

st.sidebar.subheader("新しいいちご")
st.sidebar.image('11.jpg', use_column_width=True)

if st.button("次へ", key=10000): 
    a = 1
    
num=len(lst_image)
lcol=[]
col= st.columns(5)
def syasinhyouzi():
    if st.button("↓{}".format(i+1), key=i+1): 
        df_first = df[:i]
        df_first = df_first.append(pd.Series('11.jpg', index=df.columns), ignore_index=True)
        df_second = df[i:]
        df_concat = pd.concat([df_first, df_second])
        df_concat.to_csv("result.csv", index=False ) 
    st.image(lst_image[i], use_column_width=True)
for i in list(range(0,num,5)):
    with col[0]:
        syasinhyouzi()            
for i in list(range(1,num,5)):
    with col[1]:
        syasinhyouzi()             
for i in list(range(2,num,5)):
    with col[2]:
        syasinhyouzi() 
for i in list(range(3,num,5)):
    with col[3]:
        syasinhyouzi()   
for i in list(range(4,num,5)):
    with col[4]:
        syasinhyouzi()  
        

st.title('')
st.title('')
df = pd.read_csv('result.csv',encoding='cp932')
st.download_button(label='結果ダウンロード', data=df.to_csv(), file_name='result_.csv')
