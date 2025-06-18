import streamlit as st
import pandas as pd
from utils.normalize_text import normalize_text

st.set_page_config(page_title="Text Variation Normalization", layout="centered")

st.title("Textual Variations in Social Media")
st.markdown("""
This demo illustrates challenges and solutions related to **text normalization** in noisy social media data,
based on the paper:  
📄 *Textual Variations in Social Media Text Processing Applications: Challenges, Solutions, and Trends*  
**Authors**: Jebran Khan et al. (2025)  
[View on Springer](https://link.springer.com/article/10.1007/s10462-024-11071-z)
""")

st.image("figures/taxonomy.png", caption="Taxonomy of Textual Variations", use_column_width=True)

st.header("Try Text Normalization")
user_input = st.text_input("Enter informal text (e.g., 'luv u 4ever'):")
if user_input:
    normalized = normalize_text(user_input)
    st.success(f"Normalized: `{normalized}`")

st.header("Batch Example Inputs")
if st.button("Show Examples"):
    df = pd.read_csv("examples/example_inputs.csv")
    df["Normalized"] = df["Informal"].apply(normalize_text)
    st.dataframe(df)