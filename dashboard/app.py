import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import streamlit as st
import pandas as pd
import plotly.express as px
from src.sentinelpay.data_generator import generate_transactions
from src.sentinelpay.predict import predict_one

st.set_page_config(page_title="SentinelPay", page_icon="🛡️", layout="wide")
st.title("🛡️ SentinelPay")
st.caption("AI-assisted UPI-like transaction risk monitoring | Synthetic demonstration")
if st.sidebar.button("Generate demo transactions"):
    st.session_state["demo"] = generate_transactions(1000)
df = st.session_state.get("demo", generate_transactions(500))
fraud_rate = df["is_fraud"].mean()*100
c1,c2,c3,c4 = st.columns(4)
c1.metric("Transactions", f"{len(df):,}")
c2.metric("Synthetic fraud rate", f"{fraud_rate:.2f}%")
c3.metric("Average amount", f"₹{df.amount.mean():,.0f}")
c4.metric("New-device events", f"{df.device_new.sum():,}")
st.subheader("Transaction activity")
fig = px.histogram(df, x="amount", color="is_fraud", nbins=40,
                   title="Transaction amount distribution (synthetic labels)")
st.plotly_chart(fig, use_container_width=True)
st.subheader("Recent transaction sample")
st.dataframe(df.sort_values("timestamp", ascending=False).head(30), use_container_width=True)
st.info("This dashboard visualizes synthetic labels. Train the model and use the API for model-based scoring. No live UPI connection exists.")
