import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns

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
        attribute_relationship(attribute1, attribute2, hue)
    elif not (attribute1 or attribute2 or hue):
        st.markdown("<h1 style='text-align: center; color: black; font-size: 18px;'>Heatmap of Numeric Attributes</h1>", unsafe_allow_html=True)
        numeric_attributes = df[attributes_to_select].select_dtypes(include=['float64', 'int64'])
        corr = numeric_attributes.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        fig = sns.mpl.pyplot.gcf()
        st.pyplot(fig)
        st.markdown("<h1 style='text-align: center; color: black; font-size: 18px;'>Select two attributes to show their relationship.</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align: center; color: black; font-size: 18px;'>Select two attributes to show their relationship.</h1>", unsafe_allow_html=True)
        