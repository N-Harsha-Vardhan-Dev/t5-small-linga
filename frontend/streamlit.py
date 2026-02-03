import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Linga Bot", page_icon="🧠")

st.title("🧠 Linga Bot")
st.caption("AI Grammar Correction System")

if "token" not in st.session_state:
    st.session_state.token = None

with st.expander("🔐 Authentication", expanded=True):
    mode = st.radio("Action", ["Register", "Login"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button(mode):
        endpoint = "/register" if mode == "Register" else "/login"
        res = requests.post(
            f"{BACKEND_URL}{endpoint}",
            json={"username": username, "password": password},
        )

        if res.status_code == 200:
            if mode == "Login":
                st.session_state.token = res.json()["access_token"]
                st.success("Login successful")
            else:
                st.success("Registered successfully")
        else:
            st.error(res.json().get("detail", "Request failed"))

st.divider()

text = st.text_area("Enter text to correct")
engine = st.selectbox(
    "Choose grammar engine",
    ["t5", "google"]
)

if st.button("Correct Grammar"):
    if not st.session_state.token:
        st.warning("Please login first")
    else:
        headers = {"Authorization": f"Bearer {st.session_state.token}"}
        res = requests.post(
            f"{BACKEND_URL}/correct",
            params={"text": text, "engine": engine},
            headers=headers,
        )

        if res.status_code == 200:
            st.success("Corrected Text")
            st.write(res.json()["corrected_text"])
        else:
            try:
                error_data = res.json()
                st.error(error_data.get("detail", "Error occurred"))
            except Exception:
                st.error(f"Request failed ({res.status_code})")
