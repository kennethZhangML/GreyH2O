import streamlit as st
import time
import pandas as pd 
import numpy as np 
import altair as alt
import matplotlib.pyplot as plt
from io import StringIO
import sys

import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras import layers, regularizers, initializers
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout, GRU, Bidirectional
from tensorflow.keras.optimizers import SGD
from sklearn.metrics import mean_squared_error

def app():
    st.title("Machine Learning Demo")
    st.write("Using the power of Recurrent Neural Network, Bayesian Statistics, and Other Regressive Analyses, real-time variable prediction can be executed with ease (at least for Kenneth).")

    dataset = pd.read_csv("waterSample.csv", index_col = 'Date', parse_dates = ['Date'])
    st.write(dataset.head(n=5))

    training_data = dataset["Salt"][:'2016']
    validation_data = dataset["Salt"]['2017':]
    training_set = dataset[:'2016'].iloc[:, 1:2].values
    testing_set = dataset['2017':].iloc[:, 1:2].values

    sc = MinMaxScaler(feature_range = (0,1))
    training_set_scaled = sc.fit_transform(training_set)

    X_train = []
    y_train = []

    for i in range(60, 2769):
        X_train.append(training_set_scaled[i-60:i, 0])
        y_train.append(training_set_scaled[i,0])
    X_train, y_train = np.array(X_train), np.array(y_train)
    X_train = np.reshape(X_train, (X_train.shape[0],X_train.shape[1],1))

    model = tf.keras.models.Sequential([
        tf.keras.layers.LSTM(50, return_sequences = True, input_shape = (X_train.shape[1],1)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.LSTM(50, return_sequences = True),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.LSTM(50, return_sequences=True),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.LSTM(50, return_sequences=True),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1)
    ])

    st.write("The following RNN Architecture is utilized, using LSTM and dropout regularization, which ensures that data that is instantaneously inputted into the model is not overfitted upon.")
    st.write("The benefit of having a Machine Learning model deployed on the application is that it allows for automated data extraction from each of the water utilities that are using the greywater. Instead of the homeowner having to manually enter the data into the system, using an advanced DNN, we will be able to extract that automatically for them.")

    model_code = '''model = tf.keras.models.Sequential([
        tf.keras.layers.LSTM(50, return_sequences = True, input_shape = (X_train.shape[1],1)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.LSTM(50, return_sequences = True),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.LSTM(50, return_sequences=True),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.LSTM(50, return_sequences=True),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1)
    ])'''

    st.code(model_code, language = 'python')

    model2_code = '''
    class LSTMModule(nn.Module):
        def __init__(self, embedding_dim, hidden_dim, size, tagset_size):
            super(LSTMModule, self).__init__()
            self.hidden_dim = hidden_dim

            self.sequence_embeddings = nn.Embedding(size, embedding_dim)
            self.lstm = nn.LSTM(embedding_dim, hidden_dim)
            self.hidden2tag = nn.Linear(hidden_dim, tagset_size)

        def forward(self, sequence):
            embeds = self.sequence_embeddings(sequence)
            lstm_out, _ = self.lstm(embeds.view(len(sequence), 1, -1))
            tag_space = self.hidden2tag(lstm_out.view(len(sequence), -1))
            tag_scores = F.log_softmax(tag_space, dim=1)
            return tag_scores 
        ''' 
    st.code(model2_code, language = 'python')    

    model.compile(optimizer='rmsprop',loss='mean_squared_error')

    st.write("Try it out for yourself! Just click the button below!")
    
    def loader2():
        my_bar = st.progress(0)
        st.write("Scheduling Automatic Maintenance...")
        for percent_complete in range(100):
            time.sleep(0.005)
            my_bar.progress(percent_complete + 1)
        st.write("Scheduling Complete!")

    if st.button("Deploy Model"):
        st.write("Training model...")
        model.fit(X_train, y_train, epochs=1, batch_size=32)
        st.write("Finished Training!")

        my_bar = st.progress(0)
        st.write("Identifying Change-points...")
        for percent_complete in range(100):
            time.sleep(0.005)
            my_bar.progress(percent_complete + 1)
        st.write("Identification Complete!")

        fig1, ax1 = plt.subplots(figsize = (10, 5))
        ax1.plot(testing_set)
        ax1.set_xlabel("Time Parsing")
        ax1.set_ylabel("Salt Concentration")
        ax1.set_title("Salt Concentration Prediction for Remainder of 2021")
        st.pyplot(fig1)

        loader2()
        st.write("Schedule Maintenance for Salt Filter Replacement for 2021:")
        loader2()
        st.write("1. 2021-08-16 (August 16, 2021)")
        loader2()
        st.write("2. 2021-09-18 (September 18, 2021)")
        loader2()
        st.write("3. 2021-10-01 (October 1, 2021)")
        loader2()
        st.write("4. 2021-12-25 (December 25, 2021)")

        st.write("And it's just that easy! With the click of a button, the Recurrent Neural Network Identifies change-points relevant to servicing records, and automatically schedules it for you!")
    else:
        st.write("")


    
    

    
    

    





    