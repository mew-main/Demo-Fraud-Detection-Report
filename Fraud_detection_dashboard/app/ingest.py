import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
import pandas as pd

def upload_csv():
    uploaded_file = st.file_uploader("Upload your transaction CSV", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state['transactions'] = df
        st.success("File uploaded and parsed!")
        return df
    return None 