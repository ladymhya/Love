import streamlit as st

st.set_page_config(
    page_title="A/B Test Comparison", page_icon="📈", initial_sidebar_state="expanded"
)

placeholder = st.empty()
placeholder.title("A/B Test Comparison")

with st.sidebar:

    uploaded_file = st.file_uploader("Upload CSV", type=".csv")


with st.sidebar.form("parameters"):
    st.markdown("### Parameters")
    st.radio(
        "Hypothesis type",
        options=["One-sided", "Two-sided"],
        index=0,
        key="hypothesis",
        help="TBD",
    )
    st.slider(
        "Significance level (α)",
        min_value=0.01,
        max_value=0.10,
        value=0.05,
        step=0.01,
        key="alpha",
        help=" The probability of mistakenly rejecting the null hypothesis, if the null hypothesis is true. This is also called false positive and type I error. ",
    )
    submit = st.form_submit_button("Apply changes", on_click=None)