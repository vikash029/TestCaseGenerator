

import streamlit as st
from docx import Document
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import json

st.title("ML-based Test Case Generator")

# 1. Upload requirement file
uploaded_file = st.file_uploader("Upload .docx file", type=["docx"])
if uploaded_file is not None:
    doc = Document(uploaded_file)
    requirements = [p.text.strip() for p in doc.paragraphs if p.text.strip() != '']
    df = pd.DataFrame(requirements, columns=['requirement'])
    st.write("Requirements Preview:", df)

    # 2. ML model (synthetic training data for demo)
    train_data = [
        ("User can login with valid credentials", "functional"),
        ("Password must be at least 8 characters", "boundary"),
        ("Login fails with wrong password", "negative")
    ]
    train_df = pd.DataFrame(train_data, columns=['requirement','case_type'])
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])
    pipeline.fit(train_df['requirement'], train_df['case_type'])

    # 3. Predict test case type
    df['case_type'] = df['requirement'].apply(lambda x: pipeline.predict([x])[0])
    st.write("Predicted Test Case Types:", df)

    # 4. Generate template test cases
    def generate_test_case(row, idx):
        return {
            "id": f"TC{idx+1:03}",
            "type": row['case_type'],
            "requirement": row['requirement'],
            "input": "To be filled",
            "expected_output": "To be filled"
        }

    test_cases = [generate_test_case(row, i) for i, row in df.iterrows()]
    st.write("Generated Test Cases (JSON preview):")
    st.json(test_cases)

    # 5. Download JSON
    json_str = json.dumps(test_cases, indent=4)
    st.download_button(
        label="Download Test Cases as JSON",
        data=json_str,
        file_name="generated_test_cases.json",
        mime="application/json"
    )
