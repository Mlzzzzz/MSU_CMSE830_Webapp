import streamlit as st
import pandas as pd
import similarity_webapp_molecule_viewer

def page4():
    st.markdown("<h1 style='text-align: center; color: black; font-size: 24px;'>Analysis of Misclassified Data</h1>", unsafe_allow_html=True)
    df = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Datasets/misclassified_dataset.csv")
    df = df.rename(columns={"pred_frac_simi": "pred_frac_similar"})
    st.markdown("<h1 style='color: black; font-size: 18px;'>In the original work, a Logistic Regression (LogReg) model was built to predict the similarity of molecule pair following the equation below:</h1>", unsafe_allow_html=True)
    st.markdown(r"""
                $$
                \hat{p} = \frac{e^{w_0 + w_1 t_{xt} + w_2 t_{cs}}}{1 + e^{w_0 + w_1 t_{xt} + w_2 t_{cs}}}
                $$
                """, unsafe_allow_html=True)
    st.markdown("<h1 style='color: black; font-size: 18px;'>The LogReg model(Tanimoto CDK Extended, t<sub>xt</sub>)(TanimotoCombo, t<sub>cs</sub>) was built using scikit-learn using L1 regularization with the default value for the regularization parameter (𝜆=1).</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='color: black; font-size: 18px;'>Applying this model to the dataset and find the misclassified data(molecule pair with pred_frac_similar lower than 0.5 will be labeled as 0 in pred_similar, otherwise will be labeled as 1.):</h1>", unsafe_allow_html=True)
    st.write(df)

    jsonstr = df.to_json(orient='records')
    HTML_TEMPLATE = """
        <script src="https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/1.3.3/webcomponents-lite.js"></script>
        <link rel="import" href="https://raw.githubusercontent.com/PAIR-code/facets/master/facets-dist/facets-jupyter.html">
        <facets-dive id="elem" width="1000" height="650"></facets-dive>
        <script>
            var data = {jsonstr};
            document.querySelector("#elem").data = data;
        </script>
    """.format(jsonstr=jsonstr)
    
    st.components.v1.html(HTML_TEMPLATE, width=1000, height=650)

    id_pair = st.selectbox('Select a molecule pair to get the 2D pictures:', [''] + df["id_pair"].tolist())
    if id_pair:
        similarity_webapp_molecule_viewer.twod_viewer(id_pair)
    st.markdown("<h1 style='color: black; font-size: 18px;'>For 3D structure, please access <a href='https://github.com/Mlzzzzz/MSU_CMSE830_Webapp/tree/main/Picture/3dc_conformer' target='_blank'>My GitHub Repository</a> to download the conformer file and submit it to <a href='https://www.rcsb.org/3d-view' target='_blank'>RCSB 3D-View</a>.</h1>", unsafe_allow_html=True)





