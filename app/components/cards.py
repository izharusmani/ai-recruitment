# app/components/cards.py

import streamlit as st


def metric_card(title, value, delta=None):

    html = ""

    if delta:

        html = f"""
        <p style="
            color:#fff;
            font-size:20px;
            margin-top:10px;
        ">
            {title}
        </p>
        <p style="
            color:#fff;
            font-size:28px;
            margin-top:10px;
        ">
            {value}
        </p>
        <p style="
            color:#fff;
            font-size:14px;
            margin-top:10px;
        ">
            {delta}
        </p>
        """

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:12px;
            background-color:white;
            border:1px solid #262730;
            box-shadow:0 2px 10px rgba(0,0,0,0.05);
            text-align:left;
            background:#262730;
        ">
            {html}
        </div>
        """,
        unsafe_allow_html=True
    )


def info_card(
    title,
    content
):

    st.markdown(
        f"""
        <div style="
            padding:18px;
            border-radius:10px;
            background:#f8f9fa;
            border:1px solid #ddd;
            margin-bottom:15px;
        ">
            <h4 style="
                margin-bottom:10px;
                color:#333;
            ">
                {title}
            </h4>
            <p style="
                color:#555;
                line-height:1.6;
            ">
                {content}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def candidate_card(
    candidate_name,
    email,
    score,
    recommendation
):

    color = "#28a745"

    if score < 70:
        color = "#dc3545"

    elif score < 85:
        color = "#ffc107"

    st.markdown(
        f"""
        <div style="
            padding:20px;
            border-radius:12px;
            border:1px solid #262730;
            background:white;
            margin-bottom:15px;
            box-shadow:0 2px 8px rgba(0,0,0,0.05);
            background:#262730;
        ">
            <h3 style="
                margin-bottom:5px;
            ">
                {candidate_name}
            </h3>
            <p style="
                color:#ddd;
                margin-bottom:10px;
            ">
                {email}
            </p>
            <h2 style="
                color:{color};
                margin-bottom:5px;
            ">
                AI Score: {score}
            </h2>
            <p style="
                font-weight:bold;
                color:#ddd;
            ">
                {recommendation}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )