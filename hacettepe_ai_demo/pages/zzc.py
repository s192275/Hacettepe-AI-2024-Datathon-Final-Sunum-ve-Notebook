import streamlit as st
import pandas as pd
from pickle import load
import numpy as np
import warnings
import matplotlib.pyplot as plt

warnings.warn("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)


def open_and_predict_model(path):
    model = load(open(path, 'rb'))
    start_date = pd.Timestamp('2014-05-01')
    future_index = pd.date_range(start=start_date, periods=90, freq='D')
    predictions = model.forecast(steps=len(future_index))
    predictions.reset_index(drop=True, inplace=True)
    #plt.plot(predictions)
    #plt.xlabel('Days')
    #plt.ylabel('Values')
    #plt.title('Prediction of ZZC Coin')
    #st.pyplot()    
    return predictions


zzc = "zzc_data_"

ohlc = ["open.pkl", "high.pkl", "low.pkl", "close.pkl"]
head_zzc = ["Zzc Data Open","Zzc Data High","Zzc Data Low","Zzc Data Close"]
    
for i, h in zip(ohlc, head_zzc):
    st.subheader(h)
    zzc_model = open_and_predict_model(zzc+i)
    st.write(zzc_model)
