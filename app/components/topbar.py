# app/components/topbar.py

import streamlit as st


def render_topbar(page_title):

    col1, col2, col3 = st.columns([6, 2, 2])

    # =========================
    # PAGE TITLE
    # =========================
    with col1:

        st.markdown(
            f"""
            <h1 style="
                margin-top:10px;
                margin-bottom:0px;
            ">
                {page_title}
            </h1>
            """,
            unsafe_allow_html=True
        )

    # =========================
    # SEARCH BOX
    # =========================
    with col2:

        st.text_input(
            label="Search",
            placeholder="Search...",
            label_visibility="collapsed"
        )

    # =========================
    # PROFILE AREA
    # =========================
    with col3:

        st.markdown(
            """
            <div style="
                display:flex;
                justify-content:flex-end;
                align-items:center;
                gap:10px;
                margin-top:8px;
            "><div style="
                    width:40px;
                    height:40px;
                    border-radius:50%;
                    background:#4F46E5;
                    color:white;
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    font-weight:bold;
                    font-size:16px;
                ">
                    HR
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")