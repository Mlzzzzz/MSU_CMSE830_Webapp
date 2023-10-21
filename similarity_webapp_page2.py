import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns

def show_annotation(annotation, key):
    state_key = f'show_annotation_{key}'
    
    if state_key not in st.session_state:
        st.session_state[state_key] = False

    if st.button('Annotation', key=key):
        st.session_state[state_key] = not st.session_state[state_key]

    if st.session_state[state_key]:
        st.markdown(f"<h1 style='color: black; font-size: 18px;'>{annotation}</h1>", unsafe_allow_html=True)

def page2():
    st.markdown("<h1 style='text-align: center; color: black; font-size: 24px;'>Distribution of Attributes</h1>", unsafe_allow_html=True)
    df = pd.read_csv(r"https://raw.githubusercontent.com/Mlzzzzz/MSU_CMSE830_Webapp/main/Datasets/preprocessed_dataset.csv")
    df['similar'] = df['similar'].astype(str)
    attributes_to_select = ['tanimoto_cdk_Extended', 'TanimotoCombo', 'pchembl_distance', 'target_name', 'frac_similar']
    hues_to_select = ['pair_type', 'similar']
    attribute = st.selectbox('Select an Attribute:', attributes_to_select)
    st.markdown(f"<h1 style='color: black; font-size: 18px;'>Statistics of {attribute}</h1>", unsafe_allow_html=True)
    stats_df = df[attribute].describe().reset_index()
    stats_df.columns = ['Statistic', 'Value']
    st.table(stats_df)
    st.write("")
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
            annotation1 = "From the statistics and boxplots of tanimoto_cdk_Extended, we can find that both mean and median of tanimoto_cdk_Extended are close to the threshold: 0.65. There is no missing value and few outliers in this attribute. It's also interesting to find that molecule pairs that are dis-similar in 3D also tend to dis-similar in 2D."
            show_annotation(annotation1,1)
            st.write("")
            st.write("")
            attribute_histogram(attribute, hue)
            annotation2 = 'For the histogram, it will be more intersting to group the data by "similar". In the area between 0.45-0.85, many molecule pairs with tanimoto_cdk_Extended smaller than the threshold are recognized "similar" by human. So it will be useful to focus on those molecule pairs and filter out some features of these misclassified molecule pairs.'
            show_annotation(annotation2,2)
    
    elif attribute == "TanimotoCombo":
        if hue:
            attribute_boxplot(attribute, hue)
            annotation3 = "Similar to tanimoto_cdk_Extended, both mean and median of TanimotoCombo are close to the threshold: 1.3. There is no missing value and few outliers in this attribute."
            show_annotation(annotation3,3)
            st.write("")
            st.write("")
            attribute_histogram(attribute, hue)
            annotation4 = "TanimotoCombo does not perform as well as tanimoto_cdk_Extended in distinguishing the similarity of molecular pairs. We can focus on molecule pairs with TanimotoCombo between 1-1.75."
            show_annotation(annotation4,4)

    elif attribute == "pchembl_distance":
        if hue:
            attribute_boxplot(attribute, hue)
            st.write("")
            st.write("")
            attribute_histogram(attribute, hue)
            annotation5 = 'In the original paper, the authors did not incorporate pchembl_distance into their model. However, this attribute exhibits a consistent distribution when grouped by "similar".'
            show_annotation(annotation5,5)

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
