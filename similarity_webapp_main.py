import streamlit as st
from similarity_webapp_start_page import start_page
from similarity_webapp_page1 import page1
from similarity_webapp_page2 import page2
from similarity_webapp_page3 import page3
from similarity_webapp_page4 import page4
 
if 'navigate' not in st.session_state:
    st.session_state.navigate = False

if not st.session_state.navigate:
    start_page()

else:
    pages = {
        "Introduction of the Dataset": page1,
        "Distribution of Attributes": page2,
        "Relationship of Attributes": page3,
        "Analysis of Misclassified Data": page4
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.selectbox("Go to", list(pages.keys()))

    # Call the function to draw the selected page.
    pages[selection]()