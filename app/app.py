import streamlit as st

st.set_page_config(page_title="RoadGuard AI", page_icon="🚧", layout="wide")
st.title("🚧 RoadGuard AI")
st.subheader("Intelligent Road Damage Detection & Analysis")
st.info("Initial scaffold is ready. Model inference will be connected after training.")

a, b, c = st.columns(3)
a.metric("Project", "RoadGuard AI")
b.metric("Model", "Pending")
c.metric("Dataset", "RDD2022")
