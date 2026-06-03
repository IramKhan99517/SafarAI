import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agent import agent_flow
import tempfile
from gtts import gTTS


st.set_page_config(page_title="SafarAI 🕋", layout="wide")
st.title("🕋 SafarAI – Pilgrim Assistant")

# ✅ session state
if "query" not in st.session_state:
    st.session_state.query = ""

if "response" not in st.session_state:
    st.session_state.response = ""

col1, col2 = st.columns([2, 1])

# ================= CHAT ================= #
with col1:

    st.subheader("💬 Ask AI")

    with st.form("chat_form", clear_on_submit=True):

        input_col, mic_col, send_col = st.columns([18, 1, 1])

        with input_col:
            user_input = st.text_input(
        "User Input",
        placeholder="Ask your question...",
        label_visibility="collapsed"
    )

            

        with mic_col:
            mic_clicked = st.form_submit_button("🎤")

        with send_col:
            send_clicked = st.form_submit_button("➡️")
            
# ✅ ✅ PUT SUGGESTIONS HERE (IMPORTANT)
    st.markdown("#### 💡 Suggestions:")

    suggest_col1, suggest_col2, suggest_col3 = st.columns(3)

    with suggest_col1:
        if st.button("🕋 Tawaf Guide"):
            user_input = "how to perform tawaf"

    with suggest_col2:
        if st.button("🌡️ Heat Safety"):
            user_input = "heat exhaustion precautions"

    with suggest_col3:
        if st.button("🏥 Nearby Hospital"):
            user_input = "hospital in makkah"


    # ✅ mic action
    if mic_clicked:
        user_input = "how to perform tawaf"

    # ✅ process input
    if send_clicked or mic_clicked or user_input:
        if user_input:
            st.session_state.query = user_input

            try:
                with st.spinner("🤖 Thinking..."):
                    response = agent_flow(user_input)
            except:
                response = "⚠️ Error occurred"

            st.session_state.response = response

    # ✅ display
    if st.session_state.query:
        st.markdown("### 🧑 You:")
        st.write(st.session_state.query)

        st.markdown("### 🤖 AI:")
        st.write(st.session_state.response)
        

# ✅ after showing response
if st.session_state.response:
    try:
        tts = gTTS(text=st.session_state.response)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)

        # ✅ Create tighter centered layout
        spacer1, content, spacer2 = st.columns([1, 2, 3])

        with content:
            st.audio(fp.name, format="audio/mp3")

    except:
        st.warning("⚠️ Audio unavailable")

# ================= INCIDENT ================= #
# ================= INCIDENT ================= #
with col2:

    st.subheader("🚨 Report Incident")

    incident_type = st.selectbox("Type", ["Medical", "Lost", "Crowd"])

    priority = st.selectbox(
        "Priority Level",
        ["🔴 High", "🟠 Moderate", "🟢 Low"]
    )

    incident_desc = st.text_area("Describe issue...", height=150)

    if st.button("✅ Submit"):

        if incident_desc.strip():

            # ✅ HIGH PRIORITY → FULL EMERGENCY FLOW
            if "High" in priority:

                st.error("🚨 HIGH PRIORITY INCIDENT")

                st.markdown(f"""
**Incident Type:** {incident_type}  
**Status:** Emergency Triggered  
""")

                # ✅ simulated system actions
                with st.spinner("📡 Notifying nearest emergency team..."):
                    import time
                    time.sleep(1.5)

                st.success("✅ Nearby emergency response team notified")

                st.info("🚑 Team dispatched to your location")
                st.warning("⏱️ Estimated arrival: 5–10 minutes")

            # ✅ MODERATE
            elif "Moderate" in priority:

                st.warning("⚠️ MODERATE PRIORITY INCIDENT")

                st.markdown(f"""
**Incident Type:** {incident_type}  
**Status:** Logged & Monitoring  
""")

                st.info("📌 Support team is reviewing the situation")

            # ✅ LOW
            else:

                st.success("✅ LOW PRIORITY INCIDENT")

                st.markdown(f"""
**Incident Type:** {incident_type}  
**Status:** Recorded for follow-up  
""")

        else:
            st.warning("⚠️ Please describe the issue")
# ================= FOOTER ================= #
st.markdown("---")
st.markdown(
    "<center style='color:gray;'>✨ Curated by Iram Majeed Khan ✨</center>",
    unsafe_allow_html=True
)

