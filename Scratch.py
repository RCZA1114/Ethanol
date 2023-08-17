


"""
measure = st.selectbox("Select Measurement", ('Mean', 'Standard Deviation'))
if measure == "Mean":
    wlm =df['WL(nm)'].mean()
    absm = df['Abs'].mean()
    st.write(f"The Mean of WL(nm) is {wlm} and Abs is {absm}. ")
elif measure == "Standard Deviation":
    wlm =df['WL(nm)'].std()
    absm = df['Abs'].std()
    st.write(f"The Standard Deviation of of WL(nm) is {wlm} and Abs is {absm}. ")

UCLWL = df['WL(nm)'].mean() + (3*df['WL(nm)'].std())
LCLWL = df['WL(nm)'].mean() - (3*df['WL(nm)'].std())
UCLABS = df['Abs'].mean() + (3*df['Abs'].std())
LCLABS = df['Abs'].mean() - (3*df['Abs'].std())
"""