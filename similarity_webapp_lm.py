import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

chemical_df = pd.read_csv(r'C:\Users\User\OneDrive - Michigan State University\Data Science\cmse830\CMSE830Datasets\similarity+prediction-1\dataset_Similarity_Prediction\new_dataset\new_dataset.csv')

col1, col2, col3 = st.columns([1, 1, 1])

col1.markdown("## Similarity Prediction of Chemical Structure")
col1.markdown("#### -Linqing Mo")
col1.markdown("<br>", unsafe_allow_html=True)
col1.markdown("You can explore similarities of molecule pair here!")
col1.markdown("<br>", unsafe_allow_html=True)
col1.markdown("This Web app is based on: Gandini, E.; Marcou, G.; Bonachera, F.; Varnek, A.; Pieraccini, S.; Sironi, M. Molecular Similarity Perception Based on Machine-Learning Models. Int. J. Mol. Sci. 2022, 23 (11), 6114.")

id_input = col2.text_input("Please type in the id of the molecule pair you want to explore")
if id_input: 
    try:
        id_value = int(id_input)  
        if 1 <= id_value <= 100:
            col2.success(f"You selected molecule pair {id_value}.")
            with col2.expander("Press to explore this molecule pair"):
                id = id_value - 1
                col2.markdown(f"### Target Name: {chemical_df['target_name'][id]}")
                col2.markdown(f"#### Pair type of this pair is: {chemical_df['pair_type'][id]}")
                cols_to_plot = ['tanimoto_cdk_Extended', 'TanimotoCombo', 'pchembl_distance', 'frac_similar']
                for col in cols_to_plot:
                    plt.figure(figsize=(10, 6))
                    sns.histplot(chemical_df[col], bins=30, kde=True)
                    plt.axvline(chemical_df[col].values[0], color='red', linestyle='--')
                    plt.title(f'Distribution of {col} with selected value')
                    st.pyplot(plt)
        else:
            col2.warning("Please enter a number between 1 and 100.")
    except ValueError:
        col2.warning("Please enter a valid number.")

col3.markdown("Attributes: tanimoto_cdk_Extended, TanimotoCombo, pchembl_distance, frac_similar")
attributes = ['tanimoto_cdk_Extended', 'TanimotoCombo', 'pchembl_distance', 'frac_similar']
attribute1 = col3.text_input("Please type in the first attribute that you want to explore the relationship")
attribute2 = col3.text_input("Please type in the second attribute that you want to explore the relationship")
if attribute1 and attribute2: 
    if attribute1 in attributes and attribute2 in attributes:
        col3.success("Both attributes are valid.")
        with col2.expander("Press to explore the relationship"):
            fig = sns.pairplot(chemical_df, vars=[attribute1, attribute2], hue="pair_type")
            col3.pyplot(fig) 
    else:
        col3.warning("Please enter valid attributes.")


