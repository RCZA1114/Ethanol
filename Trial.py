import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib as plt

@st.cache_data
def load_data():
    data = pd.read_csv("All Data.csv", usecols=['No.','WL(nm)','Abs','Batch'])
    

    return data

    
data = load_data()

df = pd.read_csv("All Data.csv", usecols=['No.','WL(nm)','Abs'])
batch_id = data['Batch'].unique()
selected_batch = st.selectbox('Select Batch', batch_id)
selected_batch2 = st.multiselect('Choose batches for Final Batch', options = batch_id, default=batch_id)

UCLWL = df['WL(nm)'].mean() + (3*df['WL(nm)'].std())
LCLWL = df['WL(nm)'].mean() - (3*df['WL(nm)'].std())
UCLABS = df['Abs'].mean() + (3*df['Abs'].std())
LCLABS = df['Abs'].mean() - (3*df['Abs'].std())


filtered_data2 = data[data['Batch'].isin(selected_batch2)]
wavelenght = st.slider('Select Wavelenght', value=(0, df['WL (nm)'].max()), max_value=df['WL (nm)'].max(), min_value=0, key="slider")
## filtered_data = data[data['WL(nm)'].isin(wavelenght)]

filtered_data = filtered_data[filtered_data2['WL(nm)'].isin(range(wavelenght[0], wavelenght[1]))]
#st.dataframe(filtered_data)
measure = st.selectbox("Select Measurement", ('Mean', 'Standard Deviation'))
if measure == "Mean":
    wlm =filtered_data['WL(nm)'].mean()
    absm = filtered_data['Abs'].mean()
    st.write(f"The Mean of the selected batches for WL(nm) and Abs (respectively) is {wlm}  is {absm}. ")
elif measure == "Standard Deviation":
    wlm =filtered_data['WL(nm)'].std()
    absm = filtered_data['Abs'].std()
    st.write(f"The Standard Deviation of the selected batches for WL(nm) and Abs (respectively) is {wlm}  is {absm}. ")

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


fig = px.scatter(filtered_data, x=x_axis, y=y_axis , title="Chart of the Data")
fig2 = px.scatter(df, x=x_axis, y=y_axis, title="Chart of the Data (Aggregate)", color = 'Batch')


st.plotly_chart(fig, use_container_width=True)
#st.plotly_chart(fig2, use_container_width=True)

## st.write("Out of control Values")
## st.dataframe(ooc)

x = data.groupby(['Batch'])['Abs'].mean()

st.bar_chart(x, y='Abs')
