# features/charts.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def generate_chart(df: pd.DataFrame) -> None:
    st.write("📊 Generating chart...")

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) >= 2:
        x = numeric_cols[0]
        y = numeric_cols[1]

        fig, ax = plt.subplots()
        ax.plot(df[x], df[y])
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.set_title(f"{y} vs {x}")

        st.pyplot(fig)
    else:
        st.write("Not enough numeric columns.")
