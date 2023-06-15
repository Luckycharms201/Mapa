import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Interactive Reports Map",
                   page_icon=":bar_chart:",
                   layout='wide'
                   
)

Reports = pd.read_csv('Police_Department_Incident_Reports__2018_to_Present.csv')
                      #, encoding='latin1')

# Define the number of rows to display per page
rows_per_page = 1000

# Calculate the total number of pages
num_pages = len(Reports) // rows_per_page + 1

# Get the current page number from the user
#page_number = st.number_input('Page Number', min_value=1, max_value=num_pages, value=1)

# Calculate the start and end indices of the current page
#start_index = (page_number - 1) * rows_per_page
#end_index = start_index + rows_per_page

#---------SIDEBAR------------

#st.sidebar.header('Please Filter Here:')

#year = st.sidebar.multiselect(
    #"Select the year:",
    #options=Reports['Incident Year'].unique(),
    #default=Reports['Incident Year'].unique()
#)

#neighborhood = st.sidebar.multiselect(
    #"Select the Neighborhood:",
   # options=Reports['Analysis Neighborhood'].unique(),
   # default=Reports['Analysis Neighborhood'].unique()
#)

#incident = st.sidebar.multiselect(
    #"Select the incident category:",
    #options=Reports['Incident Category'].unique(),
    #default=Reports['Incident Category'].unique()
#)

#selection = Reports.query(
   # "`Incident Year` == @year & `Analysis Neighborhood` == @neighborhood & `Incident Category` == @incident"
#)

# Display the current page of the dataframe
#st.dataframe(selection.iloc[start_index:end_index])

# -------- MAIN PAGE ---------
st.title(":earth_americas: Reports Map")
st.markdown("##")

# Get the available years
available_years = Reports['Incident Date'].dt.year.dropna().unique()

# Select a specific year
selected_year = st.selectbox('Select a year', available_years)

# Filter the data based on the selected year
filtered_data = Reports.loc[Reports['Incident Date'].dt.year == selected_year]

fig2 = px.scatter_mapbox(filtered_data, lat="Latitude", lon="Longitude", zoom=15, hover_data=["Incident Subcategory", "Incident Description", "Incident Date"])
fig2.update_layout(mapbox_style="stamen-terrain")
fig2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig2.update_layout(title='Crime Map',
                   font=dict(family='Arial', size=18),
                   plot_bgcolor='white',
                   paper_bgcolor='lightgray')


fig2.update_traces(hoverlabel=dict(font=dict(size=12), bgcolor='midnightblue', bordercolor='gold'))

# Display the figure
st.plotly_chart(fig2, use_container_width=True, use_container_height=True)
