import altair as alt
import pandas as pd
import streamlit as st


alt.data_transformers.disable_max_rows()
st.header("2023-24 Winston-Salem State University Women's Volleyball")
@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df
volleyball = load_data("WSSU Volleyball Data.csv")





dig_count = volleyball.groupby(['Date','Player'])['Digs'].count().reset_index(name='count')
opponent = st.sidebar.selectbox("Opponent",
    dig_count['Opponent'].unique().tolist())
dig_count = dig_count[dig_count['Opponent'] == opponent]
dig_count['Oppoent'] = dig_count['Opponent'].str.strip()
chart = alt.Chart(dig_count, title= f'Monthly Count of stops for {opponent}').mark_line().encode(
    alt.X('Month_of_Stop', title = 'Month of Stop'),
    alt.Y('count', title = '')
).interactive()
st.altair_chart(chart, use_container_width= True)
stops = volleyball[volleyball['Opponent'] == opponent]
st.dataframe(volleyball)