import streamlit as st
from predict_app import show_predicted_productivity
from explore_app import show_exploration
side=st.sidebar.selectbox('Predict or Explore', ('Predict', 'Explore'))
if side=='Predict':
    show_predicted_productivity()
elif side=='Explore':
    show_exploration()