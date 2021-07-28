import streamlit as st
import time
import pandas as pd 
import numpy as np 
import altair as alt
import matplotlib.pyplot as plt
from io import StringIO
import sys

import streamlit as st
import pandas as pd
import numpy as np
import changefinder 

def app():

    st.title("Advanced Anomaly Detection for Precise Multivariate Maintenance Prediction")

    st.subheader("Using Advanced Bayesian Step-wise Modelling for Anomaly Detection")

    st.write("Although our Recurrent Neural Network allows for faster, more efficient scheduling and visualization of data, it is important that we detect anomalies in greywater data.")
    st.write("Through the use of a Bayesian Step-wise Change-point model, we will be able to detect, via anomaly scores, the required maintenance for each metric.")
    st.write("Anomaly detection is crucial for accurate time series prediction of when certain greywater pollutants, such as chemicals, may reach an unacceptable concentration.")

    df = pd.read_csv("waterSample.csv")
    salt_data = df["Salt"]
    pm_data = df['PM2.5']
    volume_data = df['Volume']
    dates = df['Date']

    st.write(df)

    st.write("Here, we will create a demo, demonstrating how our Bayes Step Wise Network will perform on Salt Concentrations in the data we used previously.")
    st.write("This model does not require any prior training, as it is an unsupervised model.")
    st.write("The readiness of this model makes it more ideal for quick deployment.")

    two_cols = st.checkbox("2 columns", True)
    if two_cols:
        col1, col2 = st.beta_columns(2)

    if two_cols:
            with col1:
                st.image("images/Max.png", use_column_width = True, caption = "")
            with col2:
                st.image("images/Min.png", use_column_width = True)
    else:
        with st.beta_container():
            st.image("images/Max.png", use_column_width = True)
            st.image("images/Min.png", use_column_width=True)
    
    st.write("Right for Increasing Qualities, Left for Decreasing Qualities")
    st.write("E.S. Page 1998 ---> CUSUM Chart:")
    st.write("When Si passes a threshold that was set in advance, according to Page, the quality of the process has deteriorated too much and action should be taken; in our case, it means that the observations have changed sufficiently to detect that at some time before i, a change point has occurred. The model will therefore detect a change indicated with a spike.")

    def loader3():
        my_bar = st.progress(0)
        st.write("Activating CUSUM...")
        for percent_complete in range(100):
            time.sleep(0.005)
            my_bar.progress(percent_complete + 1)
        st.write("Creating Visualization Plot...")
        for percent_complete in range(100):
            time.sleep(0.005)
            my_bar.progress(percent_complete + 1)
        st.write("Change-points Detected!")
    
    def loader4():
        my_bar = st.progress(0)
        st.write("Writing Indexes of Anomaly Scores...")
        for percent_complete in range(100):
            time.sleep(0.005)
            my_bar.progress(percent_complete + 1)
        st.write("Listing Indexes of Unacceptable Scores!")

    def changefinderTS(data, r, order, smooth):
        cf = changefinder.ChangeFinder(r=r, order=order, smooth=smooth)

        ret = []
        for i in data:
            score = cf.update(i)
            ret.append(score)
        return ret

    def plotTSScore(data, ret):
        fig = plt.figure(figsize=(17, 8))
        ax = fig.add_subplot(111)
        loader3()
        ax.plot(ret, label='anomaly score', color = 'red', alpha=0.9)
        ax2 = ax.twinx()
        ax2.plot(data, label='real', color = 'blue', alpha=0.9)
        plt.title('Anomaly Score for Change-points')
        plt.ylabel('anomaly score')
        plt.xlabel('data count')
        st.pyplot(fig)

    option = st.selectbox('Select a Metric', options=('Please Select an Option','Salt', 'PM2.5', 'Volume'))

    if option == 'Please Select an Option':
        st.write("")
    if option == 'Salt':
        ret1 = changefinderTS(salt_data, r=0.03, order=1, smooth=5)
        plotTSScore(salt_data, ret1)
        loader4()
        st.write("These scores and their corresponding indexes will be matched with the dates that correspond to the indexes. Based on trends and seasonalities, automated servicing will be scheduled, in addition to real-time tips as to what you should use the greywater for at that instant or time period. Each range of indexes indicates the time interval (in seconds).")
        st.write("Anything greater than a score of 10.0 is considered unacceptable.")
        st.write(ret1)
    if option == 'PM2.5':
        ret2 = changefinderTS(pm_data, r=0.03, order=1, smooth=5)
        plotTSScore(pm_data, ret2)
        loader4()
        st.write("These scores and their corresponding indexes will be matched with the dates that correspond to the indexes. Based on trends and seasonalities, automated servicing will be scheduled, in addition to real-time tips as to what you should use the greywater for at that instant or time period. Each range of indexes indicates the time interval (in seconds).")
        st.write("Anything greater than a score of 10.0 is considered unacceptable.")
        st.write(ret2)
    if option == 'Volume':
        ret3 = changefinderTS(volume_data, r = 0.03, order = 1, smooth = 5)
        plotTSScore(volume_data, ret3)
        loader4()
        st.write("These scores and their corresponding indexes will be matched with the dates that correspond to the indexes. Based on trends and seasonalities, automated servicing will be scheduled, in addition to real-time tips as to what you should use the greywater for at that instant or time period. Each range of indexes indicates the time interval (in seconds).")
        st.write("Anything greater than a score of 10.0 is considered unacceptable.")
        st.write(ret3)
    else:
        st.write("")




