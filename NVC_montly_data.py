import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import openpyxl


data=pd.read_excel("MontlyImmigrationData.xlsx")

st.write(data.head())
fig,ax=plt.subplots()
ax.scatter(data['MonthYear'],data['F1'])
ax.set_xlabel('Month and Year')
ax.set_ylabel('F1 Visa Issuances')


plt.xticks(rotation=45)

# Display the plot in Streamlit
st.pyplot(fig)




