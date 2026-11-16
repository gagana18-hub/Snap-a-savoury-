import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Snap & Savory", page_icon="📸", layout="centered")

# Hide default Streamlit padding/header so the game fits cleanly on mobile
st.markdown("""
    <style>
        .block-container { padding-top: 1rem; padding-bottom: 0rem; }
        header, footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# Read and render the HTML5 game
with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=760, scrolling=False)
