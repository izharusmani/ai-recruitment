# app/components/sidebar.py

import streamlit as st
from streamlit_option_menu import option_menu


def render_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <h1 style='text-align:center;'>
                AI Recruitment
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        selected = option_menu(

            menu_title=None,

            options=[
                "Dashboard",
                "Upload Resumes",
                "Candidates",
                "Analytics"
            ],

            icons=[
                "speedometer2",
                "cloud-upload",
                "people",
                "bar-chart"
            ],

            menu_icon="cast",

            default_index=0,

            styles={

                "container": {
                    "padding": "5!important",
                    "background-color": "#262730",
                },

                "icon": {
                    "color": "#4F46E5",
                    "font-size": "18px"
                },

                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px",
                    "--hover-color": "#0e1117",
                    "border-radius": "8px"
                },

                "nav-link-selected": {
                    "background-color": "#0e1117",
                    "color": "white"
                },
            }
        )

        st.markdown("---")

        st.caption("AI Powered Recruitment System")

    return selected