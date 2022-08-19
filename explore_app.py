import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import predict_app
from predict_app import load_data
df=load_data()

def show_exploration():
    st.title('Instructions and correlations')
    st.subheader('Distance to solar noon')
    st.write('''Solar noon is the time when the Sun appears to contact the local celestial meridian.
    This is when the Sun reaches its apparent highest point in the sky, at 12 noon apparent solar time and can be observed using a sundial.
    The local or clock time of solar noon depends on the longitude and date.
    Distance to solar noon is the angle between the sun at solar noon and the a line perpendicular to the surface of solar panel.''')
    st.subheader('Visibility')
    st.write('''The visibility is the measure of the distance at which an object or light can be clearly discerned.
    In meteorology it depends on the transparency of the surrounding air and as such, it is unchanging no matter the ambient light level or time of day.''')
    st.subheader('Note')
    st.write('The higher index, the higher productivity. If we want to calculate the productivity for a certain period (day, month, year, ...), we use average values for this period (average temperature, wind speed...).' )
    
    fig1, ax1=plt.subplots()
    dfp=df.groupby('Distance to Solar Noon')['Power Generated'].mean().reset_index()
    ax1.scatter(dfp['Distance to Solar Noon'],dfp['Power Generated'])
    ax1.set_xlabel('Distance to Solar Noon')
    ax1.set_ylabel('Productivity Index')
    st.subheader('Distance to Solar Noon vs Productivity Index')
    st.pyplot(fig1)


    fig1, ax1=plt.subplots()
    dfp=df.groupby('Average Temperature (Day)')['Power Generated'].mean().reset_index()
    ax1.scatter(dfp['Average Temperature (Day)'],dfp['Power Generated'])
    ax1.set_xlabel('Average Temperature (Day)')
    ax1.set_ylabel('Productivity Index')
    st.subheader('Average Temperature (Day) vs Productivity Index')
    st.pyplot(fig1)


    fig1, ax1=plt.subplots()
    dfp=df.groupby('Average Wind Speed (Day)')['Power Generated'].mean().reset_index()
    ax1.scatter(dfp['Average Wind Speed (Day)'],dfp['Power Generated'])
    ax1.set_xlabel('Average Wind Speed')
    ax1.set_ylabel('Productivity Index')
    st.subheader('Average Wind Speed vs Productivity Index')
    st.pyplot(fig1)


    fig1, ax1=plt.subplots()
    dfp=df.groupby('Sky Cover')['Power Generated'].mean().reset_index()
    ax1.scatter(dfp['Sky Cover'],dfp['Power Generated'])
    ax1.set_xlabel('Sky Cover')
    ax1.set_ylabel('Productivity Index')
    st.subheader('Sky Cover vs Productivity Index')
    st.pyplot(fig1)

    fig1, ax1=plt.subplots()
    dfp=df.groupby('Visibility')['Power Generated'].mean().reset_index()
    ax1.scatter(dfp['Visibility'],dfp['Power Generated'])
    ax1.set_xlabel('Visibility')
    ax1.set_ylabel('Productivity Index')
    st.subheader('Visibility vs Productivity Index')
    st.pyplot(fig1)


    fig1, ax1=plt.subplots()
    dfp=df.groupby('Relative Humidity')['Power Generated'].mean().reset_index()
    ax1.scatter(dfp['Relative Humidity'],dfp['Power Generated'])
    ax1.set_xlabel('Relative Humidity')
    ax1.set_ylabel('Productivity Index')
    st.subheader('Relative Humidity vs Productivity Index')
    st.pyplot(fig1)


    fig1, ax1=plt.subplots()
    dfp=df.groupby('Average Barometric Pressure (Period)')['Power Generated'].mean().reset_index()
    ax1.scatter(dfp['Average Barometric Pressure (Period)'],dfp['Power Generated'])
    ax1.set_xlabel('Average Pressure')
    ax1.set_ylabel('Productivity Index')
    st.subheader('Pressure vs Productivity Index')
    st.pyplot(fig1)
