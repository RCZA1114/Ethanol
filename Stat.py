import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib as plt
@st.cache_data
def load_data():
    data = pd.read_csv("All Data.csv", usecols=['No.','WL(nm)','Abs','Batch'])
    

    return data

    
data = load_data()

x=data.groupby('Batch')['Abs'].mean()

plot_abs = x.plot()


st.plotly_chart(plot_abs, use_container_width=True)
