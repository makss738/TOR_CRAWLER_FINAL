import json
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Tor CTI Dashboard",
    layout="wide"
)


st.title(
    "🕷️ Tor CTI Dashboard"
)


# ==========================
# Chargement résultats
# ==========================

try:

    with open(
        "data/results.json",
        "r"
    ) as f:

        results = json.load(f)


except Exception:

    results = []



if not results:

    st.warning(
        "Aucune donnée disponible. Lance le crawler."
    )

    st.stop()



df = pd.DataFrame(results)



# ==========================
# KPI
# ==========================

col1,col2,col3 = st.columns(3)



with col1:

    st.metric(
        "Pages crawlées",
        len(df)
    )



with col2:

    total_entities = sum(
        len(x)
        for x in df["entities"]
    )

    st.metric(
        "Entités détectées",
        total_entities
    )



with col3:

    st.metric(
        "Score total",
        int(
            df["score"].sum()
        )
    )



st.divider()



# ==========================
# Résultats
# ==========================


st.subheader(
    "📊 Résultats CTI"
)



min_score = st.slider(

    "Score minimum",

    0,

    100,

    0
)



filtered = df[
    df["score"]
    >= min_score
]



st.dataframe(

    filtered[

        [
            "url",
            "status",
            "score",
            "entities",
            "signals",
            "links_found"
        ]

    ],

    use_container_width=True
)



st.divider()



# ==========================
# Alertes
# ==========================


st.subheader(
    "🚨 Alertes CTI"
)



try:

    with open(
        "data/alerts.json",
        "r"
    ) as f:

        alerts=json.load(f)


except Exception:

    alerts=[]



if not alerts:

    st.success(
        "Aucune alerte détectée"
    )


else:


    for alert in alerts:


        st.error(

f"""
URL :

{alert['url']}


Niveau :

{alert['severity']}


Score :

{alert['score']}


Entités :

{', '.join(alert['entities'])}


Signaux :

{', '.join(alert['signals'])}

Date :

{alert['timestamp']}
"""

        )
