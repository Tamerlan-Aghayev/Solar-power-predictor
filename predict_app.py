import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import PolynomialFeatures
def load_data():
    df=pd.read_csv('BigML_Dataset_5f50a4cc0d052e40e6000034.csv')
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

