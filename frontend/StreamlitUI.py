import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agent import agent_flow

# ✅ Page config
st.set_page_config(page_title="SafarAI 🕋", layout="wide")

st.title("🕋 SafarAI – Pilgrim Assistant")

# ✅ Mobile toggle (for demo)
is_mobile = st.sidebar.checkbox("📱 Mobile View", value=False)

# ✅ session state
if "query" not in st.session_state:
    st.session_state.query = ""

if "response" not in st.session_state:
    st.session_state.response = ""

# ✅ responsive layout
if is_mobile:
    col1 = st.container()
    col2 = st.container()
else:
    col1, col2 = st.columns([2, 1])

# ================= CHAT ================= #
