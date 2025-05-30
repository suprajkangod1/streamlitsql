import streamlit as st
import pandas as pd
import sqlalchemy
import os
import matplotlib.pyplot as plt

# Feature imports
from RAGToSQL.Features.query_explainability import explain_query
from RAGToSQL.Features.query_guardrails import check_query_rules
from RAGToSQL.Features.nlp_data_transformer import apply_transformation
from RAGToSQL.Features.schema_explorer import fetch_schema_overview
from RAGToSQL.Features.chat_memory import get_memory
from RAGToSQL.Features.kpi_intelligence import map_kpi_to_sql
from RAGToSQL.Features.sql_diff_explainer import explain_sql_diff
from RAGToSQL.Features.ml_plugin_system import train_ml_model
from RAGToSQL.Helper.MySQLConnection import get_sqlalchemy_uri

st.set_page_config("AI SQL Assistant", layout="wide")
st.title("🧠 AI SQL Assistant Dashboard")

# Navigation
section = st.sidebar.selectbox("🗭 Navigate to Feature", [
    "Run SQL with Explainability",
    "Check SQL Guardrails",
    "Data Transformer (NLP)",
    "Explore Schema",
    "KPI to SQL Generator",
    "SQL Diff Visualizer",
    "Train ML Model",
])

# Dummy DB engine (SQLite fallback)
uri = get_sqlalchemy_uri()
engine = sqlalchemy.create_engine(uri)

if section == "Run SQL with Explainability":
    st.subheader("Run SQL + Explain")
    sql = st.text_area("Enter SQL Query")
    if st.button("Run"):
        with engine.connect() as conn:
            df = pd.read_sql_query(sql, conn)
            st.dataframe(df)
            if not df.empty:
                st.bar_chart(df.select_dtypes(include=['number']))
                st.line_chart(df.select_dtypes(include=['number']))
        schema = fetch_schema_overview(engine)
        result = explain_query(sql, list(schema.keys()))
        st.json(result)

elif section == "Check SQL Guardrails":
    st.subheader("Test SQL against Safety Rules")
    sql = st.text_area("Enter SQL Query")
    if st.button("Check"):
        result = check_query_rules(sql)
        st.json(result)

elif section == "Data Transformer (NLP)":
    st.subheader("Upload CSV + Describe Transformations")
    uploaded = st.file_uploader("Upload CSV", type="csv")
    instruction = st.text_input("Instruction (e.g. remove nulls and lowercase)")
    if uploaded:
        df = pd.read_csv(uploaded)
        st.write("Original Data:", df)
        st.bar_chart(df.select_dtypes(include=['number']))
        if instruction:
            transformed = apply_transformation(df, instruction)
            st.write("Transformed:", transformed)
            st.bar_chart(transformed.select_dtypes(include=['number']))

elif section == "Explore Schema":
    st.subheader("Database Schema")
    schema = fetch_schema_overview(engine)
    st.json(schema)

elif section == "KPI to SQL Generator":
    st.subheader("Ask for a KPI")
    kpi = st.text_input("Example: total claims by state")
    if kpi:
        sql = map_kpi_to_sql(kpi)
        st.code(sql, language="sql")

elif section == "SQL Diff Visualizer":
    st.subheader("Compare SQL Queries")
    user_sql = st.text_area("Original SQL", height=150)
    ai_sql = st.text_area("AI SQL", height=150)
    if st.button("Compare"):
        diff = explain_sql_diff(user_sql, ai_sql)
        st.code(diff)

elif section == "Train ML Model":
    st.subheader("Train Model on Your Dataset")
    file = st.file_uploader("Upload CSV with labeled data", type="csv")
    label = st.text_input("Label column name")
    if file and label:
        df = pd.read_csv(file)
        report = train_ml_model(df, label)
        st.json(report)
        if "feature_importance" in report:
            fig, ax = plt.subplots()
            importance = report["feature_importance"]
            ax.bar(importance.keys(), importance.values())
            ax.set_title("Feature Importance")
            ax.set_ylabel("Importance")
            ax.set_xticklabels(importance.keys(), rotation=45, ha="right")
            st.pyplot(fig)