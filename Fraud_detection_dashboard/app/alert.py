import streamlit as st

def show_alerts(df):
    flagged = df[df["flagged"]]
    for idx, row in flagged.iterrows():
        with st.expander(f"Alert: {row['description']} (${row['amount']}) on {row['date']}"):
            st.write(f"**Category:** {row['category']}")
            st.write(f"**Transaction ID:** {row['transaction_id']}")
            st.write(f"**Anomaly Score:** {row['anomaly_score']}")
            feedback = st.radio(f"Is this a true positive?", ("Unmarked", "True Positive", "False Positive"), key=f"feedback_{idx}")
            if st.button("Save Feedback", key=f"save_{idx}"):
                st.session_state['feedback'][row['transaction_id']] = feedback
                st.success("Feedback saved!") 