import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(layout="wide")

st.title("📖 Data Storytelling App")

file = st.file_uploader(
    "Upload Dataset",
    type="csv"
)

if file:

    df = pd.read_csv(file)

    st.header("Dataset Introduction")

    st.write(
        f"Rows: {df.shape[0]}"
    )

    st.write(
        f"Columns: {df.shape[1]}"
    )

    st.dataframe(df.head())

    st.header("EDA")

    st.write(
        "Missing Values"
    )

    st.write(
        df.isnull().sum()
    )

    st.write(
        "Summary Statistics"
    )

    st.write(
        df.describe()
    )

    numeric = df.select_dtypes(
        include=np.number
    ).columns

    categorical = df.select_dtypes(
        exclude=np.number
    ).columns

    st.header("Visualizations")

    if len(numeric) > 0:

        fig = px.histogram(
            df,
            x=numeric[0]
        )

        st.plotly_chart(fig)

    if len(numeric) > 1:

        fig2 = px.scatter(
            df,
            x=numeric[0],
            y=numeric[1]
        )

        st.plotly_chart(fig2)

    if len(categorical) > 0:

        vc = df[
            categorical[0]
        ].value_counts().head(10)

        fig3 = px.bar(
            x=vc.index,
            y=vc.values
        )

        st.plotly_chart(fig3)

    st.header("Insights")

    st.write("""
    - Observe trends from charts
    - Compare categories
    - Detect patterns
    - Identify outliers
    """)

    st.header("Recommendations")

    st.write("""
    - Improve categories with low performance
    - Monitor unusual trends
    - Use data for future predictions
    """)

else:
    st.info("Upload CSV")