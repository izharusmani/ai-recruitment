import streamlit as st
import requests
import pandas as pd

from app.components.topbar import render_topbar
from app.components.cards import candidate_card

API_URL = "http://127.0.0.1:8000"


def candidates_page():

    render_topbar("Candidates")
    st.title("Candidates Management")
    st.markdown("---")

    # =========================
    # FETCH DATA
    # =========================
    try:
        candidates = requests.get(f"{API_URL}/candidates/").json()
        analyses = requests.get(f"{API_URL}/candidate-analysis/").json()

    except Exception as e:
        st.error(f"API Error: {str(e)}")
        candidates = []
        analyses = []

    # =========================
    # MAP ANALYSIS BY CANDIDATE ID
    # =========================
    analysis_map = {
        a["candidate_id"]: a for a in analyses
    }

    # =========================
    # SEARCH
    # =========================
    search = st.text_input("Search Candidate")

    st.markdown("---")

    table_data = []

    for candidate in candidates:

        cid = candidate.get("id")

        analysis = analysis_map.get(cid, {})

        name = candidate.get("full_name", "")
        email = candidate.get("email", "")
        phone = candidate.get("phone", "")

        # =========================
        # SEARCH FILTER
        # =========================
        if search:
            if search.lower() not in name.lower() and search.lower() not in email.lower():
                continue

        table_data.append({

            "ID": cid,
            "Name": name,
            "Email": email,
            "Phone": phone,

            # AI DATA (NOW DYNAMIC)
            "AI Score": analysis.get("score", "N/A"),
            "Recommendation": analysis.get("recommendation", "Not Evaluated"),
            "Matched Skills": analysis.get("matched_skills", ""),
            "Missing Skills": analysis.get("missing_skills", "")
        })

    # =========================
    # SUMMARY CARDS
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Candidates", len(table_data))

    with col2:
        st.metric("Shortlisted", len([x for x in table_data if x["AI Score"] != "N/A" and x["AI Score"] >= 70]))

    with col3:
        st.metric("Pending Review", len([x for x in table_data if x["AI Score"] == "N/A"]))

    st.markdown("---")

    # =========================
    # TABLE
    # =========================
    st.subheader("Candidate List")

    if table_data:
        df = pd.DataFrame(table_data)
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No candidates found")

    st.markdown("---")

    # =========================
    # PROFILE VIEW
    # =========================
    st.subheader("Candidate Profile")

    if table_data:

        candidate_names = [item["Name"] for item in table_data]

        selected_candidate = st.selectbox("Select Candidate", candidate_names)

        selected_data = next(
            (item for item in table_data if item["Name"] == selected_candidate),
            None
        )

        if selected_data:

            candidate_card(
                candidate_name=selected_data["Name"],
                email=selected_data["Email"],
                score=selected_data["AI Score"],
                recommendation=selected_data["Recommendation"]
            )

            st.markdown("---")

            col1, col2 = st.columns(2)

            with col1:
                st.info(f"Candidate ID: {selected_data['ID']}")
                st.info(f"Email: {selected_data['Email']}")

            with col2:
                st.info(f"Phone: {selected_data['Phone']}")
                st.info(f"Status: {selected_data['Recommendation']}")

            st.markdown("---")

            st.subheader("AI Analysis")

            st.write("Matched Skills:")
            st.success(selected_data.get("Matched Skills", "N/A"))

            st.write("Missing Skills:")
            st.warning(selected_data.get("Missing Skills", "N/A"))

            st.markdown("---")

            col1, col2, col3 = st.columns(3)

            with col1:
                if st.button("Shortlist"):
                    st.success("Candidate shortlisted")

            with col2:
                if st.button("Reject"):
                    st.error("Candidate rejected")

            with col3:
                if st.button("Schedule Interview"):
                    st.info("Interview scheduled")