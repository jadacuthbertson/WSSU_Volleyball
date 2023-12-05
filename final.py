import altair as alt
import pandas as pd
import streamlit as st


st.title("2023-24 Winston-Salem State University Women's Volleyball")

volleyball_df = pd.read_csv("WSSU Volleyball Data.csv")
st.dataframe(volleyball_df)

scatter = alt.Chart(volleyball_df).mark_point().encode(
    alt.X("Position", title = "Position"),
    alt.Y("Attack Errors", title = "Attack Errors")
)
st.altair_chart(scatter, use_container_width=True)