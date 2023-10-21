import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
from similarity_webapp_page2 import show_annotation

def page3():
    st.markdown("<h1 style='text-align: center; color: black; font-size: 24px;'>Relationship of Attributes</h1>", unsafe_allow_html=True)
    df = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Datasets/preprocessed_dataset.csv")
    df['similar'] = df['similar'].astype(str)
    attributes_to_select = ['tanimoto_cdk_Extended', 'TanimotoCombo', 'pchembl_distance', 'target_name', 'frac_similar']
    hues_to_select = ['pair_type', 'similar']
    attribute1 = st.selectbox('Select the First Attribute for X Axis:', [''] + attributes_to_select)
    attribute2 = st.selectbox('Select the Second Attribute for Y Axis:', [''] + [attribute for attribute in attributes_to_select if attribute != attribute1])
    hue = st.selectbox('Select a Hue:', [''] + hues_to_select)

    def attribute_relationship(attribute1, attribute2, hue):
            st.markdown("<h1 style='text-align: center; color: black; font-size: 18px;'>You can drag to select the area you want to specify on the graph.</h1>", unsafe_allow_html=True)
            st.write("")
            st.write("")

            brush = alt.selection_interval()
            base = alt.Chart(df).add_params(brush)

            unique_hues = df[hue].nunique()
            soft_colors = sns.color_palette("muted", unique_hues).as_hex()

            points = base.mark_circle().encode(
            x=alt.X(attribute1, axis=alt.Axis(title='')),
            y=alt.Y(attribute2, axis=alt.Axis(title='')),
            color=alt.condition(brush, alt.Color(f"{hue}:N", scale=alt.Scale(range=soft_colors)), alt.value('grey'))
            ).properties(
                title={
                    "text": f"Scatter Plot of {attribute1} and {attribute2} Grouped by {hue}"
                }
            )
            tick_axis = alt.Axis(labels=False, domain=False, ticks=False)
            x_ticks = base.mark_tick().encode(
                alt.X(attribute1, axis=tick_axis),
                alt.Y(hue, title='', axis=tick_axis),
                color=alt.condition(brush, alt.Color(f"{hue}:N", scale=alt.Scale(range=soft_colors)), alt.value('lightgrey'))
            )
            y_ticks = base.mark_tick().encode(
                alt.X(hue, title='', axis=tick_axis),
                alt.Y(attribute2, axis=tick_axis),
                color=alt.condition(brush, alt.Color(f"{hue}:N", scale=alt.Scale(range=soft_colors)), alt.value('lightgrey'))
            )

            final_chart = y_ticks | (points & x_ticks)
            st.altair_chart(final_chart, use_container_width=True)
    
    if attribute1 and attribute2 and hue:
        if attribute1 == "tanimoto_cdk_Extended":
            if attribute2 == "TanimotoCombo":
                attribute_relationship(attribute1, attribute2, hue)
                annotation2 = 'When changing hues between "similar" and "pair_type", we can notice that all the "sim2D, sim3D" and "Dis2D, Dis3D" molecule pairs are correctly recognized. In the "dis2D, sim3D" area, the wrongly recognized pairs are concentrated around 1.4&lt;TanimotoCombo&lt;1.65 area.'
                show_annotation(annotation2,2)
            if attribute2 == "pchembl_distance":
                attribute_relationship(attribute1, attribute2, hue)
            if attribute2 == "target_name":
                attribute_relationship(attribute1, attribute2, hue)
            if attribute2 == "frac_similar":
                attribute_relationship(attribute1, attribute2, hue)
                annotation3 = 'As the heatmap shown, there is a strong positive relationship between tanimoto_cdk_Extended and frac_similar. An interesting fact is that comparing to "dis2D, sim3D" group, most "sim2D, dis3D" group are correctly recognized. An possible explanation is that when doing web survey, humans can only get access to the 2D picture rather than the 3D conformer.'
                show_annotation(annotation3,3)
        if attribute1 == "TanimotoCombo":
            if attribute2 == "tanimoto_cdk_Extended":
                attribute_relationship(attribute1, attribute2, hue)
                annotation4 = 'When changing hues between "similar" and "pair_type", we can notice that all the "sim2D, sim3D" and "Dis2D, Dis3D" molecule pairs are correctly recognized. In the "dis2D, sim3D" area, the wrongly recognized pairs are concentrated around 1.4&lt;TanimotoCombo&lt;1.65 area.'
                show_annotation(annotation4,4)
            if attribute2 == "pchembl_distance":
                attribute_relationship(attribute1, attribute2, hue)
            if attribute2 == "target_name":
                attribute_relationship(attribute1, attribute2, hue)
            if attribute2 == "frac_similar":
                attribute_relationship(attribute1, attribute2, hue)
                annotation5 = 'As the heatmap shown, there is also a strong positive relationship between TanimotoCombo and frac_similar.'
                show_annotation(annotation5,5)
        if attribute1 == "pchembl_distance":
            if attribute2 == "frac_similar":
                attribute_relationship(attribute1, attribute2, hue)
                annotation6 = 'All molecule pair with pchembl_distance&gt;1.45 are recognized as "dissimilar".'
                show_annotation(annotation6,6)
            else:
                attribute_relationship(attribute1, attribute2, hue)
        if attribute1 == "target_name":
            attribute_relationship(attribute1, attribute2, hue)
        if attribute1 == "frac_similar":
            attribute_relationship(attribute1, attribute2, hue)
    elif not (attribute1 or attribute2 or hue):
        st.markdown("<h1 style='text-align: center; color: black; font-size: 18px;'>Heatmap of Numeric Attributes</h1>", unsafe_allow_html=True)
        numeric_attributes = df[attributes_to_select].select_dtypes(include=['float64', 'int64'])
        corr = numeric_attributes.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        fig = sns.mpl.pyplot.gcf()
        st.pyplot(fig)
        annotation1 = "Both tanimoto_cdk_Extended and TanimotoCombo have a high positive correlation to frac_similar, suggesting a strong positive relationship between 2D similarity, 3D similarity and molecule pair similarity."
        show_annotation(annotation1,1)
        st.markdown("<h1 style='text-align: center; color: black; font-size: 18px;'>Select two attributes to show their relationship.</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align: center; color: black; font-size: 18px;'>Select two attributes to show their relationship.</h1>", unsafe_allow_html=True)
        