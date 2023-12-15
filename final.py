import altair as alt
import pandas as pd
import streamlit as st
import plotly.express as px

alt.data_transformers.disable_max_rows()

col1, col2, col3 = st.columns(3)
with col1:
    st.write(' ')

with col2:

    st.image('WSSU Logo.jpg',use_column_width='auto')

with col3:
    st.write(' ')

st.markdown("<h1 style='text-align: center; color: black;'>Women's Volleyball Statistics</h1>", unsafe_allow_html=True)

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df
volleyball = load_data("WSSU Volleyball Data.csv")


opponent = volleyball['Opponent'].unique() # get the unique values of the opponent column
opponent_choice = st.selectbox('Select an Opponent', opponent) # create a selectbox widget
filtered_df = volleyball.loc[volleyball['Opponent'] == opponent_choice] # filter the dataframe by the selected value
#st.dataframe(filtered_df) # display the filtered dataframe


fig = px.treemap(filtered_df, path = ['Player'], values = 'Aces', width = 450, height = 450, color = "Aces", color_continuous_scale=["white","red"])
fig.update_layout(title = f'Service Aces for {opponent_choice}')
fig.data[0].textinfo = 'label+text+value'
fig


position = volleyball['Position'].unique() # get the unique values of the opponent column
filtered_df2 = volleyball.loc[volleyball['Position'] == "Defensive Specialist"] # filter the dataframe by the selected value



line_chart = alt.Chart(filtered_df2, title= "Digs for Defensive Specialist").mark_line().encode(
        alt.X("Date", title = "Date"),
        alt.Y("Digs", title = "Count"),
        color="Player"
).interactive()
st.altair_chart(line_chart, use_container_width=True)


position = volleyball['Position'].unique() # get the unique values of the opponent column
filtered_df3 = volleyball.loc[volleyball['Position'] == "Setter/Rightside Hitter"] # filter the dataframe by the selected value


scatter_chart = alt.Chart(filtered_df3, title= "Assists for Setter/Rightside Hitter").mark_point().encode(
        alt.X("Assists"),
        alt.Y("Player"),
        #color="Opponent"
).interactive()
st.altair_chart(scatter_chart, use_container_width=True)





position = volleyball['Position'].unique() # get the unique values of the opponent column
position_choice = st.selectbox('Select a Position', position) # create a selectbox widget
filtered_df4 = volleyball.loc[volleyball['Position'] == position_choice] # filter the dataframe by the selected value

bar_chart = alt.Chart(filtered_df4, title= f'Count of Kills for {position_choice}').mark_bar().encode(
        alt.X("Kills"),
        alt.Y("Player")
).interactive()
st.altair_chart(bar_chart, use_container_width=True)



