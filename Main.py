import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib as plt

st.set_page_config(
    page_title="Pythos Ethanol Data",
    page_icon=":chart:",
)


st.title("Ethanol Dashboard")

@st.cache_data
def load_data():
    data = pd.read_csv("All Data.csv", usecols=['No.','WL(nm)','Abs','Batch'])

    data = data[data['Batch'] != 'Batch 8 (Part 2)']

    data = data.replace({'Batch': {'Batch 8 (Part 1)': 'Batch 8'}})

    return data

    
data = load_data()

df = pd.read_csv("All Data.csv", usecols=['No.','WL(nm)','Abs'])
batch_id = data['Batch'].unique()

## selected_batch = st.selectbox('Select Batch', batch_id)\
selected_batch = st.multiselect('Choose batches for Final Batch', options = batch_id)

UCLWL = df['WL(nm)'].mean() + (3*df['WL(nm)'].std())
LCLWL = df['WL(nm)'].mean() - (3*df['WL(nm)'].std())
UCLABS = df['Abs'].mean() + (3*df['Abs'].std())
LCLABS = df['Abs'].mean() - (3*df['Abs'].std())


filtered_data = data[data['Batch'].isin(selected_batch)]

wavelenght = st.slider('Select Wavelenght', value=(0, 800), max_value=800, min_value=0, key="slider")
## filtered_data = data[data['WL(nm)'].isin(wavelenght)]

filtered_data = filtered_data[filtered_data['WL(nm)'].isin(range(wavelenght[0], wavelenght[1]))]
data = data[data['WL(nm)'].isin(range(wavelenght[0], wavelenght[1]))]
#st.dataframe(filtered_data)

filtered_data['WL_lim'] = 0
filtered_data.loc[filtered_data['WL(nm)'] > ((filtered_data['WL(nm)'].mean()) + (3*(filtered_data['WL(nm)'].std()))), 'WL_lim'] = 1
filtered_data.loc[filtered_data['WL(nm)'] < ((filtered_data['WL(nm)'].mean()) - (3*(filtered_data['WL(nm)'].std()))), 'WL_lim'] = 1

filtered_data['Abs_lim'] = 0
filtered_data.loc[filtered_data['Abs'] > ((filtered_data['Abs'].mean()) + (3*(filtered_data['Abs'].std()))), 'Abs_lim'] = 1
filtered_data.loc[filtered_data['Abs'] < ((filtered_data['Abs'].mean()) - (3*(filtered_data['Abs'].std()))), 'Abs_lim'] = 1


## st.write(f" The number of out of control products in 'Abs' is {filtered_data['Abs_lim'].sum()} and  'WL' is {filtered_data['WL_lim'].sum()}.")

ooc = filtered_data[filtered_data['Abs_lim']==1]


x_axis = st.selectbox('Select X axis',('No.','WL(nm)','Abs'))

y_axis = st.selectbox('Select Y axis',('No.','WL(nm)','Abs'))


fig = px.scatter(filtered_data, x=x_axis, y=y_axis , title=f"Chart of the Data for the selected batches", color = 'Batch')
fig2 = px.scatter(data, x=x_axis, y=y_axis, title="Chart of the Data (All Batches)", color = 'Batch')


st.plotly_chart(fig, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)

## st.write("Out of control Values")
## st.dataframe(ooc)

x = data.groupby(['Batch'])['Abs'].mean()

st.write("Bar Chart of the Batch Means for 'Abs'.")
st.bar_chart(x, y='Abs')
