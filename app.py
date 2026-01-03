import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

st.set_page_config(layout="wide")
st.title("📊 ICT PD Array Dashboard")

DATA_FOLDER = "data"

@st.cache_data
def load_csv(path):
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    return df

files = sorted([f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")])

pair = st.selectbox("Select Market", files)

df = load_csv(os.path.join(DATA_FOLDER, pair))

fig = go.Figure(
    data=[go.Candlestick(
        x=df.index,
        open=df["open"],
        high=df["high"],
        low=df["low"],
        close=df["close"]
    )]
)

fig.update_layout(
    height=700,
    xaxis_rangeslider_visible=False
)

st.plotly_chart(fig, use_container_width=True)
