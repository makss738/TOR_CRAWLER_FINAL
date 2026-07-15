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



try:

    with open(
        "data/results.json",
        "r"
    ) as f:

        results=json.load(f)


except:

    results=[]



if not results:

    st.warning(
        "Aucune donnée disponible"
    )

    st.stop()



df=pd.DataFrame(results)



# =====================
# KPI
# =====================


c1,c2,c3,c4 = st.columns(4)



with c1:

    st.metric(
        "Pages",
        len(df)
    )



with c2:

    st.metric(

        "Entités",

        sum(
            len(x)
            for x in df["entities"]
        )

    )



with c3:

    st.metric(

        "Score total",

        int(
            df["score"].sum()
        )

    )



with c4:

    changed=len(
        df[
            df["content_changed"]
            ==
            True
        ]
    )

    st.metric(
        "Modifications",
        changed
    )



st.divider()



# =====================
# TABLE
# =====================


st.subheader(
    "📊 Résultats CTI"
)



st.dataframe(

    df[

        [

            "url",

            "status",

            "score",

            "level",

            "entities",

            "signals",

            "hash",

            "content_changed"

        ]

    ],

    use_container_width=True

)



st.divider()



# =====================
# ALERTES
# =====================


st.subheader(
    "🚨 Alertes"
)



alerts=df[

    df["score"] > 0

]



if len(alerts)==0:


    st.success(
        "Aucune alerte"
    )


else:


    for _,row in alerts.iterrows():


        st.error(

f"""
URL :

{row['url']}


Niveau :

{row['level']}


Score :

{row['score']}


Entités :

{', '.join(row['entities'])}


Signaux :

{', '.join(row['signals'])}

"""

        )



st.divider()



# =====================
# HASH MONITORING
# =====================


st.subheader(
    "🔄 Surveillance des changements"
)



changes=df[

    df["content_changed"]

    ==

    True

]



if len(changes)==0:


    st.success(
        "Aucune modification détectée"
    )


else:


    st.warning(

        f"{len(changes)} pages modifiées"

    )


    st.dataframe(

        changes[

            [

                "url",

                "hash"

            ]

        ],

        use_container_width=True

    )
