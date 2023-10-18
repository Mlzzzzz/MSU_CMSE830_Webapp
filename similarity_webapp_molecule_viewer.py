import streamlit as st

def format_number(n):
    if n < 10:
        return "00" + str(n)
    elif n < 100:
        return "0" + str(n)
    else:
        return str(n)

def twod_viewer(n):
    n_str = format_number(n)

    twod_urla = f"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Picture/image_molecule_{n_str}a.svg"
    twod_urlb = f"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Picture/image_molecule_{n_str}b.svg"

    col1, col2 = st.columns(2)
    col1.markdown(f"<img src={twod_urla} width='400' height='250' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
    col2.markdown(f"<img src={twod_urlb} width='400' height='250' alt='Statins' style='display: block; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)
