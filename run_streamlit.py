import streamlit as st

from app.components.sidebar import render_sidebar

from app.views.dashboard import dashboard_page
from app.views.upload import upload_page
from app.views.candidates import candidates_page
from app.views.analytics import analytics_page

st.set_page_config(
    page_title="AI Recruitment Agent",
    layout="wide"
)

menu = render_sidebar()

if menu == "Dashboard":
    dashboard_page()

elif menu == "Upload Resumes":
    upload_page()

elif menu == "Candidates":
    candidates_page()

elif menu == "Analytics":
    analytics_page()