import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

def app():
    st.title("About OUR Team")

    two_cols = st.checkbox("2 columns", True)
    if two_cols:
        col1, col2 = st.beta_columns(2)

    if two_cols:
            with col1:
                st.image("images/kenneth.png", use_column_width = True, caption = "Kenneth Zhang - The Tech Lead")
            with col2:
                st.image("images/Emily.jpg", use_column_width = True, caption = "Emily Lau - The Delegate")
            with col1:
                st.image("images/Erica.jpg", use_column_width = True, clamp = True, caption = "Erica Power - The Educator")
            with col2:
                st.image("images/Yash.jpeg", use_column_width = True, caption = "Yash the Analyst")
            with col1:
                st.image("images/Andrea.png", use_column_width = True, caption = "Andrea the Creative Editor")
            with col2:
                st.image("images/Amy.jpg", use_column_width = True, caption = "Amy the Devil's Advocate")
            with col1:
                st.image("images/Brianna.jpg", use_column_width = True, caption = "Brianna the Ideation Master")
            with col2:
                st.image("images/Adriana.jfif", use_column_width = True, caption = "Da Best Facilitator")
    else:
        with st.beta_container():
            st.image("images/kenneth.png", use_column_width = True, caption = "Kenneth is a meme")
    

