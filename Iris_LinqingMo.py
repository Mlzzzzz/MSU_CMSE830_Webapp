import streamlit as st
import seaborn as sns
import plotly.express as px

iris_df = sns.load_dataset("iris")
st.write("""
# Iris Dataset Visualization
The classic Iris dataset has four features: sepal length, sepal width, petal length, and petal width.
    This app visualizes the dataset in an interactive 3D scatter plot, in which the size of a dot represents the petal width of an Iris flower.
""")
fig = px.scatter_3d(iris_df, 
                    x='sepal_length', 
                    y='sepal_width', 
                    z='petal_length', 
                    color='species',
                    size='petal_width',
                    hover_data=['species'])
    
st.plotly_chart(fig)
