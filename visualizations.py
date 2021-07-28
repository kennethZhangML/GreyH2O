import streamlit as st
import time
import pandas as pd 
import numpy as np 
import altair as alt
import matplotlib.pyplot as plt

def app():    
    with st.beta_container():
        st.title("Visualizations")
        st.header("Plots for Utilities Visualizations")
        st.write("""See the code and plots for five utilities at once.""")

    dataset = pd.read_csv("waterSample.csv")
    dataset['Date'] = pd.to_datetime(dataset['Date'])

    def loader():
        my_bar = st.progress(0)
        st.write("Extracting Data from utilities...")
        for percent_complete in range(100):
            time.sleep(0.005)
            my_bar.progress(percent_complete + 1)
        st.write("Extraction Complete!")
    
    st.write(dataset)
    dates = dataset['Date']
    salt_data = dataset["Salt"]
    chemical_data = dataset["Chemicals"]
    pm_data = dataset["PM2.5"]
    volume_data = dataset["Volume"]    
    
    two_cols = st.checkbox("2 columns", True)
    if two_cols:
        col1, col2 = st.beta_columns(2)
    
    if two_cols:
        with col1:
            st.subheader("Salt Data")
            st.line_chart(data = salt_data, use_container_width=True)
        with col2:
            st.subheader("Volume Data")
            st.line_chart(data = volume_data, use_container_width=True)
        with col1:
            st.subheader("Chemicals")
            st.line_chart(data = chemical_data, use_container_width=True)
        with col2:
            st.subheader("Salt Data")
            st.line_chart(data = salt_data, use_container_width=True)
        with col1:
            st.subheader("PM2.5 Data")
            st.line_chart(data = pm_data, use_container_width=True)
        with col2:
            st.subheader("All Data")
            st.line_chart(data = dataset, use_container_width=True)
    else:
        with st.beta_container():
            loader()
            st.subheader("Salt Data")
            st.line_chart(data = salt_data, use_container_width=True)

            loader()
            st.subheader("Chemical Data")
            st.line_chart(data = chemical_data, use_container_width=True)

            loader()
            st.subheader("Volume Data")
            st.line_chart(data = volume_data, use_container_width=True)

    fig1, ax1 = plt.subplots(figsize = (10, 5))
    ax1.plot(salt_data)
    ax1.set_xlabel("Salt Concentration")
    ax1.set_ylabel("Seconds Parse")
    ax1.set_title("Salt Concentration Time Series Analysis")
    st.pyplot(fig1)

    fig2, ax1 = plt.subplots(figsize = (10, 5))
    ax1.plot(volume_data)
    ax1.set_xlabel("PM2.5 Concentration")
    ax1.set_ylabel("Seconds Parse")
    ax1.set_title("PM2.5 Concentration Time Series Analysis")
    st.pyplot(fig2)

    st.subheader("Real Time Analysis")
    st.write("Real time data extraction from home water utilities.")
    st.write("In order to minimize the involvement of the homeowner in data collection, our system automatically collects data via a DNN-centralized system.")
    st.write("This is so that the homeowner can live in peace, without having to worry about whether or not data was actually collected. Who doesn't wanna live in peace?")

    loader()
    st.subheader("Salt Concentration Levels")
    st.line_chart(data = salt_data, use_container_width=True)

    loader()
    st.subheader("Chemical Concentration Levels")
    st.line_chart(data = chemical_data, use_container_width=True)

    loader()
    st.subheader("Usage Volume")
    st.line_chart(data = volume_data, use_container_width=True)
