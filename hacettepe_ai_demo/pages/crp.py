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
    #plt.title('Prediction of CRP Coin')
    #st.pyplot()    
    return predictions

crp = "crp_data_"

ohlc = ["open.pkl", "high.pkl", "low.pkl", "close.pkl"]
head_crp = ["Crp Data Open", "Crp Data High", "Crp Data Low", "Crp Data Close"]
    
for i, h in zip(ohlc, head_crp):
    st.subheader(h)
    crp_model = open_and_predict_model(crp+i)
    st.write(crp_model)

