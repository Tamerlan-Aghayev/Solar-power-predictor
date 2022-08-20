import streamlit as st

side=st.sidebar.selectbox('Predict or Explore', ('Predict', 'Explore'))
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import PolynomialFeatures
def load_data():
    df=pd.read_csv('https://www.kaggle.com/datasets/vipulgote4/solar-power-generation?select=BigML_Dataset_5f50a4cc0d052e40e6000034.csv')
    df=df[df['Power Generated']!=0]
    df.drop(['Day of Year', 'Year', 'Month', 'Day', 'First Hour of Period', 'Is Daylight','Average Wind Speed (Period)', 'Average Wind Direction (Day)'], axis=1, inplace=True)
    df['Average Barometric Pressure (Period)']=df['Average Barometric Pressure (Period)']*3386.39/100
    df['Average Temperature (Day)']=(df['Average Temperature (Day)']-32)/180*100
    df.dropna(axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df
df=load_data()
transformer=PolynomialFeatures(degree=3)
final_model=Ridge(alpha=0.005)
train=transformer.fit_transform(df.drop('Power Generated', axis=1))
final_model.fit(train, df['Power Generated'])
def show_predicted_productivity():
    st.title("Solar Panel Productivity Prediction")
    st.write("""### Please input the parameters""")
    distance_to_solar_noon = st.number_input('Distance to solar noon (in radians): ', format="%.6f")
    temperature = st.number_input('Temperature (in degrees Celsius): ')
    average_wind_speed=st.number_input('Average wind speed (in m/s): ')
    sky_cover=st.slider('Sky cover (asses from 0 to 4): ', 0,4,1)
    visibility=st.number_input('Visibility (in kms): ')
    relative_humidity=st.number_input('Relative humidity (in percentages): ')
    average_barometric_pressure=st.number_input('Average Barmoetric Pressure (in mmHg): ')
    ok=st.button('Calculate productivity index of solar panel location')
    if ok:
        ls=list(df.columns)
        ls.remove('Power Generated')
        x=pd.DataFrame(columns=ls)
        
        x=x.append({'Distance to Solar Noon':distance_to_solar_noon,'Average Temperature (Day)':temperature,'Average Wind Speed (Day)':average_wind_speed,'Sky Cover':sky_cover,'Visibility':visibility,'Relative Humidity':relative_humidity,'Average Barometric Pressure (Period)':average_barometric_pressure}, ignore_index=True)
        x=x.astype(np.float64)
        x=transformer.fit_transform(x)
        
        
        index_of_productivity=final_model.predict(x)
        st.subheader(f'The estimated productivity index is {index_of_productivity[0]}')




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

if side=='Predict':
    show_predicted_productivity()
elif side=='Explore':
    show_exploration()
