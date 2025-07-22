# AI-Driven Fraud Detection Dashboard (MVP)

## Overview
This project is an interactive dashboard that simulates fraud detection by analyzing transaction data. It demonstrates core concepts in fraud, risk management, data-driven product strategy, and how AI tools can automate and enhance decision-making. Built for portfolio and learning purposes.

## Project Goal
- Build a Streamlit dashboard for uploading and analyzing transaction data
- Detect anomalies using simple ML (Z-score or Isolation Forest)
- Allow user feedback to improve detection
- Visualize alerts and trends

## Target Audience
- Hiring Managers (AI, FinTech, RiskOps)
- Technical Teams (data pipelines, ML basics, system architecture)
- PM Community (product thinking, builder mindset)

## Features
- **Data Ingestion:** Upload and parse CSV files
- **Anomaly Detection:** Flag suspicious transactions using ML
- **Alerting:** Display alert cards for flagged transactions
- **Memory:** Save user feedback (true/false positive) to local JSON
- **Visual Dashboard:** Charts for alert volume, types, and anomaly scores
- **Configurable Profile:** Set known recurring charges and thresholds in JSON

## Tech Stack
- Python, Streamlit, Jupyter, scikit-learn, pandas, Plotly/Seaborn/Matplotlib

## Folder Structure
```
Fraud_detection_dashboard/
│
├── .venv/                         # Python virtual environment (excluded via .gitignore)
├── config/
│   └── recurring_config.json      # JSON config for recurring charges
├── data/
│   └── sample_transactions.csv    # Mock transaction dataset
├── notebooks/
│   └── detect_anomalies.ipynb     # ML logic and data exploration
├── app/
│   ├── dashboard.py               # Streamlit app
│   ├── ingest.py                  # CSV upload & parsing logic
│   ├── detect.py                  # Anomaly detection logic
│   ├── alert.py                   # Alert creation logic
│   └── memory.py                  # Saves user feedback to JSON
├── assets/
│   └── screenshots/               # Portfolio visuals
├── .gitignore                     # Exclude .venv, local files
└── README.md                      # Overview & setup instructions
```

## Setup Instructions
1. Clone the repo and navigate to the folder:
   ```
   git clone <repo-url>
   cd Fraud_detection_dashboard
   ```
2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Mac/Linux:
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the dashboard:
   ```
   streamlit run app/dashboard.py
   ```

## Usage
- Upload a CSV of transactions (see `data/sample_transactions.csv` for format)
- The dashboard will parse and display a summary
- Outliers are flagged and shown in alert cards
- Mark alerts as accurate or false positives; feedback is saved to JSON
- Visualizations update in real time

## Config File (`config/recurring_config.json`)
- Add known recurring charges to avoid false positives and set threshold amounts 
- Example:
  ```json
  [
    {"name": "Netflix", "frequency": "monthly", "threshold": 20.00},
    {"name": "Chewy", "frequency": "monthly", "threshold": 25.00}
  ]
  ```

## User Stories
- As a user, I want to upload my transactions and see which ones are suspicious, so I can review them quickly.
- As a user, I want to mark flagged transactions as false positives, so the system learns from my feedback.
- As a user, I want to see charts of alerts and trends over time.
- As a user, I want to set recurring charges (e.g. monthly streaming services)
- As a user, I want the recurring charges to support a 'max threshold amount' to assist with fraud detection

## Success Metrics
- The app should flag at least 2 outliers in the sample data.
- User feedback should update the memory file and dashboard in real time.

## Lessons Learned
- Document your process and what you learned at each milestone.

## Future Enhancements
- Add login simulation (Streamlit Auth or Firebase)
- Connect to SQLite DB for persistent memory
- Add classification model (fraud vs. non-fraud)
- Generate natural language explanations for alerts
- Deploy online with Streamlit Cloud

## Resetting Feedback
- To reset feedback, delete or clear the `app/feedback.json` file.

## Assets
- Add screenshots or a short video of the app in action to `assets/screenshots/`. 