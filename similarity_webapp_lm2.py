import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def start_page():
    st.title("Welcome to the Molecular Similarity Analysis Web App")
    st.write("This web app provides a detailed exploration and interactive visualization \
              of the Molecular Similarity Perception dataset. To begin, click the 'Start Exploration' button below.")
    st.write("- By Linqing Mo, Michigan State University")

    if st.button('Start Exploration'):
        st.session_state.navigate = True

def page1():
    st.title("Page 1: Introduction of Dataset")
    st.write("In this part, I will elucidates the columns in this dataset using an example of a molecular pair.")

def page2():
    st.title("Page 2: Distribution of Attributes")
    st.write("In this part, I will use an interactive Altair Scatter Plot and Histogram\
             with Interval Selection to display the distribution of tanimoto_cdk_Extended, TanimotoCombo, and\
              frac_similar, with the scatter color determined by the pair_type or the mapped frac_similar. ")

def page3():
    st.title("Page 3: Relationship of Attributes")
    st.write("In this part, I will an interactive Altair Scatter Plot with LOESS Lines,\
              enabling users to select any two columns to explore their relationships.")
    
def page4():
    st.title("Page 4: Wrongly Labeled Data")
    st.write("In this part, users to explore 'incorrectly labeled' molecular pairs from the original\
              paper, providing all the IDs of the 'incorrectly labeled' molecular pairs. \
             Users can access the 2D picture and 3D interactive model of the molecular pair, \
             exploring the reasoning behind its incorrect labeling by the machine learning method \
             of the original paper.")

if 'navigate' not in st.session_state:
    st.session_state.navigate = False

if not st.session_state.navigate:
    start_page()

else:
    pages = {
        "Introduction of Dataset": page1,
        "Distribution of Attributes": page2,
        "Relationship of Attributes": page3,
        "Analysis of Wrongly Labeled Data": page4
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.selectbox("Go to", list(pages.keys()))

    # Call the function to draw the selected page.
    pages[selection]()