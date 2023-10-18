import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns

def page2():
    st.markdown("<h1 style='text-align: center; color: black; font-size: 24px;'>Distribution of Attributes</h1>", unsafe_allow_html=True)
    df = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Datasets/preprocessed_dataset.csv")
    df['similar'] = df['similar'].astype(str)
    attributes_to_select = ['tanimoto_cdk_Extended', 'TanimotoCombo', 'pchembl_distance', 'target_name', 'frac_similar']
    hues_to_select = ['pair_type', 'similar']
    attribute = st.selectbox('Select an Attribute:', attributes_to_select)
    hue = st.selectbox('Select a Hue:', hues_to_select)

    def attribute_boxplot(attribute, hue):

        chart_without_hue = alt.Chart(df).mark_boxplot().encode(
            y=attribute
        ).properties(
            title=f'Boxplot of {attribute}'
        )
        
        chart_with_hue = alt.Chart(df).mark_boxplot().encode(
            x=hue,
            y=attribute
        ).properties(
            title=f'Boxplot of {attribute} Grouped by {hue}'
        )
        
        combined_chart = alt.hconcat(chart_without_hue, chart_with_hue)
        st.altair_chart(combined_chart, use_container_width=True)
    
    def attribute_histogram(attribute, hue):
        unique_hues = df[hue].nunique()
        soft_colors = sns.color_palette("pastel", unique_hues).as_hex()
        
        attr_min = df[attribute].min()
        attr_max = df[attribute].max()

        base = alt.Chart(df).transform_bin(
            'binned_attr', attribute, bin=alt.Bin(maxbins=20, extent=[attr_min, attr_max])
        ).transform_aggregate(
            count='count()',
            groupby=['binned_attr', hue]
        ).transform_calculate(
            bin_range="round(datum.binned_attr * 100) / 100 + '-' + round((datum.binned_attr + 1/20) * 100) / 100"
        )

        bars = base.mark_bar().encode(
            x=alt.X('bin_range:N', axis=alt.Axis(title=attribute)),
            y='count:Q',
            color=alt.Color(hue, scale=alt.Scale(range=soft_colors)),  
            order=alt.Order(
                hue,
                sort='ascending'
            )
        ).properties(
            title={
                "text": f"Histogram of {attribute} Grouped by {hue}"
            }
        )

        st.altair_chart(bars, use_container_width=True)
    
    if attribute == "tanimoto_cdk_Extended":
        if hue:
            attribute_boxplot(attribute, hue)
            st.write("")
            st.write("")
            attribute_histogram(attribute, hue)
    
    elif attribute == "TanimotoCombo":
        if hue:
            attribute_boxplot(attribute, hue)
            st.write("")
            st.write("")
            attribute_histogram(attribute, hue)

    elif attribute == "pchembl_distance":
        if hue:
            attribute_boxplot(attribute, hue)
            st.write("")
            st.write("")
            attribute_histogram(attribute, hue)

    elif attribute == "target_name":
        if hue:
            unique_hues = df[hue].nunique()
            soft_colors = sns.color_palette("pastel", unique_hues).as_hex()

            bars = alt.Chart(df).mark_bar().encode(
                x=alt.X('target_name', axis=alt.Axis(title='target_name')),
                y=alt.Y('count():Q', axis=alt.Axis(title='count')),
                color=alt.Color(hue, scale=alt.Scale(range=soft_colors)),  
                order=alt.Order(
                    hue,
                    sort='ascending'
                )
            ).properties(
                title={
                    "text": f"Histogram of target_name Grouped by {hue}"
                }
            )
            st.altair_chart(bars, use_container_width=True)

    elif attribute == "frac_similar":
        if hue:
            attribute_boxplot(attribute, hue)
            st.write("")
            st.write("")
            attribute_histogram(attribute, hue)
