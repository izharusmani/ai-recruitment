# app/views/upload.py

import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


def upload_page():

    st.title("Bulk Resume Upload")

    st.markdown("---")

    # =========================
    # FETCH JOBS
    # =========================
    try:

        jobs_response = requests.get(
            f"{API_URL}/jobs/"
        )

        jobs = jobs_response.json()

    except Exception as e:

        st.error(f"Failed to load jobs: {str(e)}")

        jobs = []

    # =========================
    # JOB SELECTION
    # =========================
    job_options = {}

    for job in jobs:

        job_options[
            f"{job['title']} ({job['company']})"
        ] = job["id"]

    selected_job = st.selectbox(
        "Select Job",
        options=list(job_options.keys())
    ) if job_options else None

    st.markdown("---")

    # =========================
    # FILE UPLOADER
    # =========================
    uploaded_files = st.file_uploader(
        "Upload Multiple Resumes",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    # =========================
    # SHOW SELECTED FILES
    # =========================
    if uploaded_files:

        st.subheader("Selected Files")

        for file in uploaded_files:

            st.write(f"📄 {file.name}")

    st.markdown("---")

    # =========================
    # START ANALYSIS BUTTON
    # =========================
    if st.button("Start AI Analysis"):

        if not selected_job:

            st.error("Please select a job")

            return

        if not uploaded_files:

            st.error("Please upload resumes")

            return

        # =========================
        # PREPARE MULTIPART FILES
        # =========================
        files = []

        for file in uploaded_files:

            files.append(
                (
                    "files",
                    (
                        file.name,
                        file.getvalue(),
                        file.type
                    )
                )
            )

        # =========================
        # FORM DATA
        # =========================
        data = {
            "job_id": job_options[selected_job]
        }

        # =========================
        # API CALL
        # =========================
        with st.spinner("AI Agent is analyzing resumes..."):

            try:

                response = requests.post(
                    f"{API_URL}/resumes/upload",
                    files=files,
                    data=data
                )
                result = response.json()
                print("POST Response:", result)

                if response.status_code == 200:

                    result = response.json()

                    st.success(
                        result["message"]
                    )

                    st.markdown("---")

                    st.subheader("Analysis Results")

                    for item in result["results"]:

                        with st.container():

                            st.info(
                                f"""
                                Candidate: {item.get('candidate_name')}

                                Email: {item.get('email')}

                                Resume Status: {item.get('resume_status')}

                                AI Score: {item.get('ai_score')}

                                Recommendation: {item.get('recommendation')}
                                """
                            )

                else:

                    st.error(
                        f"Upload Failed: {response.text}"
                    )

            except Exception as e:

                st.error(
                    f"Error: {str(e)}"
                )