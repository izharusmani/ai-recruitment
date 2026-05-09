# app/views/analytics.py

import streamlit as st
import requests
import pandas as pd
import plotly.express as px

from app.components.topbar import render_topbar
from app.components.cards import metric_card


API_URL = "http://127.0.0.1:8000"


def analytics_page():

    # =========================
    # TOPBAR
    # =========================
    render_topbar("Analytics")

    st.title("Recruitment Analytics Dashboard")

    st.markdown("---")

    # =========================
    # FETCH CANDIDATES
    # =========================
    try:

        candidates_response = requests.get(
            f"{API_URL}/candidates/"
        )

        candidates = candidates_response.json()

    except Exception as e:

        st.error(
            f"Failed to load analytics: {str(e)}"
        )

        candidates = []

    # =========================
    # SAMPLE ANALYTICS
    # =========================
    total_candidates = len(candidates)

    shortlisted = 25

    rejected = 10

    pending = 15

    # =========================
    # DASHBOARD METRICS
    # =========================
    col1, col2, col3, col4 = st.columns(4)

    with col1:

        metric_card(
            title="Total Candidates",
            value=total_candidates,
            delta="+15%"
        )

    with col2:

        metric_card(
            title="Shortlisted",
            value=shortlisted,
            delta="+10%"
        )

    with col3:

        metric_card(
            title="Rejected",
            value=rejected,
            delta="-5%"
        )

    with col4:

        metric_card(
            title="Pending",
            value=pending,
            delta="+3%"
        )

    st.markdown("---")

    # =========================
    # PIE CHART
    # =========================
    st.subheader(
        "Candidate Status Distribution"
    )

    pie_data = pd.DataFrame({

        "Status": [
            "Shortlisted",
            "Rejected",
            "Pending"
        ],

        "Count": [
            shortlisted,
            rejected,
            pending
        ]
    })

    pie_chart = px.pie(

        pie_data,

        names="Status",

        values="Count",

        hole=0.4,

        title="Candidate Hiring Funnel"
    )

    st.plotly_chart(
        pie_chart,
        use_container_width=True
    )

    st.markdown("---")

    # =========================
    # BAR CHART
    # =========================
    st.subheader(
        "Recruitment Performance"
    )

    bar_data = pd.DataFrame({

        "Category": [
            "Candidates",
            "Shortlisted",
            "Rejected",
            "Pending"
        ],

        "Count": [
            total_candidates,
            shortlisted,
            rejected,
            pending
        ]
    })

    bar_chart = px.bar(

        bar_data,

        x="Category",

        y="Count",

        text_auto=True,

        title="Recruitment Summary"
    )

    st.plotly_chart(
        bar_chart,
        use_container_width=True
    )

    st.markdown("---")

    # =========================
    # AI SCORE DISTRIBUTION
    # =========================
    st.subheader(
        "AI Candidate Score Analysis"
    )

    score_data = pd.DataFrame({

        "Candidate": [
            "John Doe",
            "Jane Smith",
            "Michael",
            "David",
            "Emma"
        ],

        "AI Score": [
            92,
            75,
            60,
            85,
            45
        ]
    })

    score_chart = px.line(

        score_data,

        x="Candidate",

        y="AI Score",

        markers=True,

        title="AI Candidate Scores"
    )

    st.plotly_chart(
        score_chart,
        use_container_width=True
    )

    st.markdown("---")

    # =========================
    # SKILL ANALYTICS
    # =========================
    st.subheader(
        "Top Skills Found in Resumes"
    )

    skills_data = pd.DataFrame({

        "Skill": [
            "Python",
            "Laravel",
            "React",
            "Docker",
            "FastAPI"
        ],

        "Candidates": [
            40,
            32,
            28,
            20,
            18
        ]
    })

    skills_chart = px.bar(

        skills_data,

        x="Skill",

        y="Candidates",

        text_auto=True,

        title="Top Technical Skills"
    )

    st.plotly_chart(
        skills_chart,
        use_container_width=True
    )

    st.markdown("---")

    # =========================
    # RECENT ANALYTICS TABLE
    # =========================
    st.subheader(
        "Recent Candidate Analytics"
    )

    analytics_table = pd.DataFrame({

        "Candidate": [
            "John Doe",
            "Jane Smith",
            "Michael",
            "David"
        ],

        "AI Score": [
            92,
            75,
            60,
            85
        ],

        "Recommendation": [
            "Strong Match",
            "Good Match",
            "Average",
            "Strong Match"
        ],

        "Status": [
            "Shortlisted",
            "Pending",
            "Rejected",
            "Shortlisted"
        ]
    })

    st.dataframe(
        analytics_table,
        use_container_width=True
    )

    st.markdown("---")

    # =========================
    # DOWNLOAD REPORT
    # =========================
    st.subheader(
        "Export Analytics"
    )

    csv = analytics_table.to_csv(
        index=False
    )

    st.download_button(

        label="Download Analytics CSV",

        data=csv,

        file_name="recruitment_analytics.csv",

        mime="text/csv"
    )