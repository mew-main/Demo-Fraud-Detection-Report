import streamlit as st
import pandas as pd
import plotly.express as px
from ingest import upload_csv
from detect import load_config, detect_anomalies
from alert import show_alerts
from memory import save_feedback, load_feedback

st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")
st.title("AI-Driven Fraud Detection Dashboard")

if 'feedback' not in st.session_state:
    st.session_state['feedback'] = load_feedback()

config = load_config("../config/recurring_config.json")
df = upload_csv()

if df is not None:
    df = detect_anomalies(df, config)
    st.subheader("Transaction Summary")
    st.dataframe(df)
    st.subheader("Flagged Transactions")
    show_alerts(df)
    if st.button("Save All Feedback"):
        save_feedback(st.session_state['feedback'])
        st.success("All feedback saved!")
    st.subheader("Visualizations")
    # Alerts over time
    flagged = df[df['flagged']]
    if not flagged.empty:
        fig = px.histogram(flagged, x='date', title='Flagged Transactions Over Time')
        st.plotly_chart(fig, use_container_width=True)
    # Amounts by category
    fig2 = px.box(df, x='category', y='amount', title='Transaction Amounts by Category')
    st.plotly_chart(fig2, use_container_width=True) 