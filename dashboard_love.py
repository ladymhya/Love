import streamlit as st
import pandas as pd
from PIL import Image
from datetime import datetime
import plotly.express as px

st.set_page_config(
    page_title="Ma Cla", page_icon="❤️"
)

placeholder = st.empty()

placeholder.title("Ma Cla ❤️")

image = Image.open('love.jpg')

st.image(image, caption='Noi')

st.write("Ciao Cla! Faccio tutto questo solo per ricordarti quanto sono smielato e noioso 😘")

df = pd.read_csv("ds1.csv")


df_last_visit = df[df["visti"] == 1]
first_visit = df_last_visit["data"].min()
first_visit = datetime.strptime(first_visit, "%Y-%m-%d")
last_visit = df_last_visit["data"].max()
last_visit = datetime.strptime(last_visit, "%Y-%m-%d")

# difference between dates in timedelta
delta_1 = datetime.now() - first_visit
delta_2 = datetime.now() - last_visit

st.header('Numeri importanti')

col1, col2 = st.columns(2)

col1.metric("Da quanti giorni ci sentiamo 💕", delta_1.days)
col2.metric("Da quanti giorni non ci vediamo 😭", delta_2.days)

st.header('Statistiche importanti')

st.write("Messaggi scambiati ogni giorno")
fig = px.histogram(df, x="data", y="count_messaggi", nbins=df.shape[0])
st.plotly_chart(fig, use_container_width=True)

st.write("Ti amo scambiatici")
fig = px.histogram(df, x="data", y="count_ti_amo", nbins=df.shape[0])
st.plotly_chart(fig, use_container_width=True)

st.write("Incontri")
fig = px.histogram(df, x="data", y="visti", nbins=df.shape[0])
st.plotly_chart(fig, use_container_width=True)
