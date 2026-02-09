import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/analyze"

st.set_page_config(page_title="CI Risk Validator", page_icon="🧠", layout="centered")

st.title("🧠 CI Pipeline Risk Validator")
st.write("Upload a CI pipeline JSON file to analyze risk before execution.")

uploaded_file = st.file_uploader("Upload pipeline JSON", type=["json"])

if uploaded_file is not None:
    if st.button("Analyze Pipeline"):
        progress_bar = st.progress(0)
        status_text = st.empty()

        files = {
            "file": (uploaded_file.name, uploaded_file.getvalue(), "application/json")
        }

        try:
            # Simulated progress while backend works
            status_text.text("Starting analysis...")
            progress_bar.progress(10)

            import time
            time.sleep(0.3)

            status_text.text("Validating syntax and schema...")
            progress_bar.progress(30)
            time.sleep(0.3)

            status_text.text("Extracting features...")
            progress_bar.progress(55)
            time.sleep(0.3)

            status_text.text("Running ML risk prediction...")
            progress_bar.progress(75)

            response = requests.post(BACKEND_URL, files=files)

            status_text.text("Finalizing results...")
            progress_bar.progress(90)

            time.sleep(0.2)

            if response.status_code == 200:
                result = response.json()

                progress_bar.progress(100)
                status_text.text("Analysis complete ✅")

                risk_level = result.get("risk_level", "UNKNOWN")
                score = result.get("final_risk_score", 0)

                if risk_level == "LOW":
                    st.success(f"✅ LOW RISK ({score} / 100)")
                elif risk_level == "MEDIUM":
                    st.warning(f"⚠️ MEDIUM RISK ({score} / 100)")
                else:
                    st.error(f"🚨 HIGH RISK ({score} / 100)")

                st.subheader("Detailed Report")
                st.json(result)

            else:
                progress_bar.empty()
                status_text.empty()
                st.error(f"Backend error: {response.text}")

        except Exception as e:
            progress_bar.empty()
            status_text.empty()
            st.error(f"Could not connect to backend: {e}")
