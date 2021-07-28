import home
import visualizations
import machineLearning
import aboutTeam
import advancedMachineLearning
import streamlit as st

PAGES = {
    "Home": home,
    "Data Extraction Demo": visualizations,
    "Machine Learning Demo": machineLearning,
    "Advanced ML Demo": advancedMachineLearning,
    "About Our Team": aboutTeam
}


st.set_page_config(layout="centered", page_icon = 'images/goated.png')
st.image("images/goated.png", caption = "It's not YOUR water, it's not MY water, it's OURwater")

st.markdown(
    """
<style>
.sidebar .sidebar-content {
    color: black;
}  
</style>
""",
    unsafe_allow_html=True,
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.sidebar.title('Navigation')
st.sidebar.image("images/goated.png", use_column_width=True, caption = "It's not YOUR water, it's not MY water, it's OURwater")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

st.sidebar.subheader("About the Developer:")
st.sidebar.write("OURwater is a software company dedicated to developing software and ML-architectures dedicated to water conservation and greywater usage promotion.")

st.sidebar.subheader("About the Demo: ")
st.sidebar.write("This is for demonstration purposes only. This is used to demonstrate the different features of the GreyH2O app that would be integrated into both the web application, and IOS and Android application platforms.")

st.write()
st.write()
st.write()
st.sidebar.write("Developed and Engineered by OURwater © Copyright 2021")

page = PAGES[selection]
page.app()