import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from streamlit_player import st_player

def app():
    st.image("images/group.png", use_column_width = True, caption = "This is our team, our team is great")

    st.subheader("Introduction")

    st.write("The Problem: Water is the most valuable natural resource for life on Earth, and Canada contains much of the Earth’s freshwater. The average Canadian water footprint is much higher than the world's average, hence, we must ask: How might we help Canadians treat our freshwater with more respect? Every day Canadian homeowners use clean drinking water for appliances such as dishwashers, laundry machines, and showers. A method has been developed to help Canadians save drinking water for one purpose and reuse water for powering day-to-day appliances. The water reused is called grey water, it is clean waste water from showers, dishwashers, etc, excluding toilets. The lack of water literacy among homeowners and the assumption that grey water contains pathogens that cannot be removed leaves many wary about the long-term benefits of this solution and leaves many concerned with the current status.") 
    st.write("With this in mind, how might we help Canadian homeowners take advantage of grey water?")

    st.subheader("Our solution")
    st.write("Our solution is an app called GreyH2O that incorporates technological advancements in AI, Data Visualization, and automatic data extraction from a home. By utilizing the power of AI, our system will be able to classify incoming data into the utility categories, such as toilets, showers, and sinks. By doing so, homeowners will easily be able to track important data about the water in their homes and manage their water usage accordingly. Daily visualizations will be provided to the consumer that helps them understand their water usage in designated partitions of their home. This includes the home’s overall efficiency score, water usage score, etc. ")

    st.subheader("The Potential Impact")
    st.write("The app GreyH2O will help Canadians delegate their drinking water for its one purpose while ensuring that this water is not being deprived from Indigenous communities. Clean drinking water is a basic human right that Indigenous people cannot easily access due to colonization. One issue contributing to this issue is Canadian’s excessive use of clean water for dishwashers and other appliances. Since our app tracks the amount of water used and recycled by Canadians, it simplifies the process of saving drinking water for the user. Thus, clean drinking water can be better distributed among all communities in Canada.")
    
    st.subheader("3-Minute Pitch Video")
    st_player("https://youtu.be/sjhoF7ob1Lk")

    st.write()
    st.write()
    st.write()
    st.write("Creators: Amy Zeng, Andrea Barreto, Brianna Davidson, Emily Lau, Erica Power, Kenneth Zhang, Ryan Zhang ----- Da Best Facilitator: Adrianna Gurreri")
    st.write("ML Engineer & Demo Dev: Kenneth Zhang")


    
