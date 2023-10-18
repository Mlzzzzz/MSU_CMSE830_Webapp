import streamlit as st

def start_page():
    st.markdown("<h1 style='text-align: center; color: black; font-size: 36px;'>Welcome to the Molecular Similarity Analysis Web App</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>This web app provides a detailed exploration and interactive visualization of the Molecular Similarity Perception dataset.</p>", unsafe_allow_html=True)

    st.markdown("<h2 style='font-size: 24px;'>Why do we care about Molecular Similarity?</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.markdown("""
        <p style='text-align: center; font-size: 14px;'>Statins</p>
        <img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Picture/Lovastatin.svg' width='200' height='100' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>
        <p style='text-align: center; font-size: 16px;'>Familial hypercholesterolemia</p>
    """, unsafe_allow_html=True)

    col2.markdown("""
        <p style='text-align: center; font-size: 14px;'>Cuprimine</p>
        <img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Picture/Penicillamine_structure.svg' width='120' height='100' alt='Cuprimine' style='display: block; margin-left: auto; margin-right: auto;'>
        <p style='text-align: center; font-size: 16px;'>Wilson's disease</p>
    """, unsafe_allow_html=True)

    col3.markdown("""
        <p style='text-align: center; font-size: 14px;'>Nebcin</p>
        <img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Picture/Tobramycin.svg' width='200' height='100' alt='Nebcin' style='display: block; margin-left: auto; margin-right: auto;'>
        <p style='text-align: center; font-size: 16px;'>Cystic fibrosis</p>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-size: 18px;'>An  <span style='color: blue; font-weight: bold;'>orphan drug</span> is a pharmaceutical agent that is developed to treat certain rare medical conditions. An orphan drug would not be profitable to produce without government assistance, due to the small population of patients affected by the conditions. </p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>One of the most important government intervention is Exclusivity (enhanced patent protection and marketing rights).</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>When developing a new orphan drug, the first thing to do is to compare it's similarity with other orphan drugs in the Exclusivity period.</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1.markdown("<img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Picture/image_molecule_003a.svg' width='300' height='150' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    col2.markdown("<img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Picture/image_molecule_003b.svg' width='300' height='150' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Are they similar?</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1.markdown("<img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Picture/image_molecule_005a.svg' width='300' height='150' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    col2.markdown("<img src='https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Picture/image_molecule_005b.svg' width='300' height='150' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Or, are they similar?</p>", unsafe_allow_html=True)

    st.markdown("<p style='font-size: 18px;'>Even experienced chemists often make mistakes!</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>Conventionally, specialists make majority votes for government to determine if two molecules are similar.</p>", unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.markdown("<p style='font-size: 18px;'>In this web app, you may get an intuition on how to build a more robust and objective system to identify molecule similarity.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 18px;'>To begin, click the 'Start Exploration' button below.</p>", unsafe_allow_html=True)
    if st.button('Start Exploration'):
        st.session_state.navigate = True
    st.write("")
    st.write("")
    st.markdown("""
    <p style='font-size: 18px;'>The original dataset is collected and built based on: Gandini, E.; Marcou, G.; Bonachera, F.; Varnek, A.; Pieraccini, S.; Sironi, M. Molecular Similarity Perception Based on Machine-Learning Models. <i>Int. J. Mol. Sci.</i> <b>2022</b>, 23, 6114.</p>
    """, unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<p style='font-size: 18px;'>Developed by Linqing Mo, Michigan State University</p>", unsafe_allow_html=True)