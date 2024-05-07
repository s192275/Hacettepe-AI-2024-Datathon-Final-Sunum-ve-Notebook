import streamlit as st
import pandas as pd
from pickle import load
import numpy as np
import warnings

warnings.warn("ignore")
st.set_page_config(
    page_title="Hacettepe AI Group Sample Application",  
    layout="centered"
)
st.title("Exchange Price Prediction App")
st.write("We care your investments...")

texts = ['BK Coin Prediction', 'CRP Coin Prediction', 'FRX Coin Prediction', 'ZZC Prediction',]
links = ['bk', 'crp', 'frx', 'zzc']
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"<div style='text-align: center;'><a href='/{links[0]}'>{texts[0]}</a></div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div style='text-align: center;'><a href='/{links[1]}'>{texts[1]}</a></div>", unsafe_allow_html=True)

with col3:
    st.markdown(f"<div style='text-align: center;'><a href='/{links[2]}'>{texts[2]}</a></div>", unsafe_allow_html=True)

with col4:
    st.markdown(f"<div style='text-align: center;'><a href='/{links[3]}'>{texts[3]}</a></div>", unsafe_allow_html=True)

