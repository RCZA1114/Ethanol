import streamlit as st
import plotly.express as px
import pandas as pd

@st.cache_data
def load_data():
    data = pd.read_csv("All Data.csv", usecols=['No.','WL(nm)','Abs','Batch'])
    

    return data

    
data = load_data()


plot_abs = data.groupby(by = "Abs").mean().plot(kind = "bar")


st.plotly_chart(plot_abs, use_container_width=True)
