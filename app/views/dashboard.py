# app/views/dashboard.py

import streamlit as st
import requests

from app.components.topbar import render_topbar
from app.components.cards import metric_card


API_URL = "http://127.0.0.1:8000"


def dashboard_page():

    # =========================
    # TOPBAR
    # =========================
    render_topbar("Dashboard")

    st.markdown("## AI Recruitment Dashboard")

    st.markdown("---")

    # =========================
    # FETCH DATA
    # =========================
    try:

        candidates_response = requests.get(
            f"{API_URL}/candidates/"
        )

        jobs_response = requests.get(
            f"{API_URL}/jobs/"
        )

        candidates = candidates_response.json()

        jobs = jobs_response.json()

        total_candidates = len(candidates)

        total_jobs = len(jobs)

    except Exception as e:

        st.error(f"API Error: {str(e)}")

        total_candidates = 0

        total_jobs = 0

        candidates = []

        jobs = []

    # =========================
    # DASHBOARD CARDS
    # =========================
    col1, col2, col3, col4 = st.columns(4)

    with col1:

        metric_card(
            "Total Candidates",
            total_candidates,
            "+12%"
        )

    with col2:

        metric_card(
            title="Active Jobs",
            value=total_jobs,
            delta="+5%"
        )

    with col3:

        metric_card(
            title="AI Shortlisted",
            value="25",
            delta="+8%"
        )

    with col4:

        metric_card(
            title="Rejected",
            value="10",
            delta="-2%"
        )

    st.markdown("---")

    # =========================
    # RECENT CANDIDATES
    # =========================
    st.subheader("Recent Candidates")

    if total_candidates > 0:

        table_data = []

        for candidate in candidates:

            table_data.append({

                "ID": candidate.get("id"),

                "Name": candidate.get("full_name"),

                "Email": candidate.get("email"),

                "Phone": candidate.get("phone")
            })

        st.dataframe(
            table_data,
            use_container_width=True
        )

    else:

        st.warning("No candidates found")

    st.markdown("---")

    # =========================
    # RECENT JOBS
    # =========================
    st.subheader("Recent Jobs")

    if total_jobs > 0:

        job_table = []

        for job in jobs:

            job_table.append({

                "ID": job.get("id"),

                "Title": job.get("title"),

                "Company": job.get("company_name")
            })

        st.dataframe(
            job_table,
            use_container_width=True
        )

    else:

        st.warning("No jobs found")