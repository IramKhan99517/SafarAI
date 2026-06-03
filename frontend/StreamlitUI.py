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
with col1:

    st.subheader("💬 Ask AI")

    # ✅ FORM
    with st.form("chat_form", clear_on_submit=True):

        # ✅ Responsive input layout
        if is_mobile:
            input_col = st.container()
            mic_col = st.container()
            send_col = st.container()
        else:
            input_col, mic_col, send_col = st.columns([8, 1, 1])

        # ✅ Input
        with input_col:
            user_input = st.text_input(
                "User Input",
                placeholder="Ask your question...",
                label_visibility="collapsed"
            )

        # ✅ Buttons
        if is_mobile:
            mic_clicked = st.form_submit_button("🎤")
            send_clicked = st.form_submit_button("➡️")
        else:
            with mic_col:
                mic_clicked = st.form_submit_button("🎤")

            with send_col:
                send_clicked = st.form_submit_button("➡️")

    # ✅ Suggestions (correct placement)
    st.markdown("#### 💡 Suggestions:")

    if is_mobile:
        if st.button("🕋 Tawaf Guide"):
            user_input = "how to perform tawaf"

        if st.button("🌡️ Heat Safety"):
            user_input = "heat exhaustion precautions"

        if st.button("🏥 Nearby Hospital"):
            user_input = "hospital in makkah"
    else:
        s1, s2, s3 = st.columns(3)

        with s1:
            if st.button("🕋 Tawaf Guide"):
                user_input = "how to perform tawaf"

        with s2:
            if st.button("🌡️ Heat Safety"):
                user_input = "heat exhaustion precautions"

        with s3:
            if st.button("🏥 Nearby Hospital"):
                user_input = "hospital in makkah"

    # ✅ Mic shortcut
    if mic_clicked:
        user_input = "how to perform tawaf"

    # ✅ Process input
    if send_clicked or mic_clicked or user_input:
        if user_input:
            st.session_state.query = user_input

            try:
                with st.spinner("🤖 Thinking..."):
                    response = agent_flow(user_input)
            except:
                response = "⚠️ Error occurred"

            st.session_state.response = response

    # ✅ Display response
    if st.session_state.query:
        st.markdown("---")

        st.markdown("### 🧑 You:")
        st.write(st.session_state.query)

        st.markdown("### 🤖 AI:")
        st.write(st.session_state.response)

# ================= INCIDENT ================= #
with col2:

    st.subheader("🚨 Report Incident")

    incident_type = st.selectbox("Type", ["Medical", "Lost", "Crowd"])

    incident_desc = st.text_area(
        "Describe issue...",
        height=150
    )

    if st.button("✅ Submit"):
        if incident_desc.strip():
            st.success("✅ Incident reported!")
        else:
            st.warning("⚠️ Please describe the issue")

# ================= FOOTER ================= #
st.markdown("---")
st.markdown(
    "<center style='color:gray;'>✨ Curated by Iram Majeed Khan ✨</center>",
    unsafe_allow_html=True
)
