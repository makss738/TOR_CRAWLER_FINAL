import streamlit as st
import json
import pandas as pd

# -------------------------
# LOAD DATA
# -------------------------
def load_data():
    try:
        with open("data/results.json", "r") as f:
            return json.load(f)
    except:
        return []

data = load_data()

# -------------------------
# UI
# -------------------------
st.set_page_config(page_title="CTI Dashboard", layout="wide")

st.title("🕵️ CTI Dark Web Monitoring Dashboard")

st.write("Analyse des données collectées via crawler Tor")

# -------------------------
# STATS GLOBALES
# -------------------------
total_pages = len(data)
total_entities = sum(len(d.get("entities", [])) for d in data)
avg_score = sum(d.get("score", 0) for d in data) / total_pages if total_pages > 0 else 0

col1, col2, col3 = st.columns(3)

col1.metric("Pages crawled", total_pages)
col2.metric("Entities detected", total_entities)
col3.metric("Avg Threat Score", round(avg_score, 2))

st.divider()

# -------------------------
# TABLE DES DONNÉES
# -------------------------
st.subheader("📊 Results Table")

if data:

    df = pd.DataFrame(data)

    st.dataframe(df, use_container_width=True)

else:
    st.warning("No data available. Run crawler first.")

# -------------------------
# FILTER ENTITIES
# -------------------------
st.subheader("🔎 Filter by entity")

all_entities = list(set(
    e for d in data for e in d.get("entities", [])
))

selected = st.selectbox("Choose entity", ["All"] + all_entities)

if selected != "All":
    filtered = [d for d in data if selected in d.get("entities", [])]
else:
    filtered = data

st.write(f"Results: {len(filtered)}")

st.dataframe(pd.DataFrame(filtered), use_container_width=True)

# -------------------------
# HIGH RISK ALERTS
# -------------------------
st.subheader("🚨 High Risk Alerts (Score >= 10)")

alerts = [d for d in data if d.get("score", 0) >= 10]

if alerts:
    st.error(f"{len(alerts)} critical findings")

    st.dataframe(pd.DataFrame(alerts), use_container_width=True)
else:
    st.success("No high risk alerts detected")


