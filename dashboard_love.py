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

st.write("Ciao Cla! Faccio tutto questo solo perchè ti amo...")

df = pd.read_csv("ds1.csv")

first_contact = df["data"].min()
first_contact = datetime.strptime(first_contact, "%Y-%m-%d")

last_contact = df["data"].max()
last_contact = datetime.strptime(last_contact, "%Y-%m-%d")

df_last_visit = df[df["visti"] == 1]
last_visit = df_last_visit["data"].max()
last_visit = datetime.strptime(last_visit, "%Y-%m-%d")

# difference between dates in timedelta
delta_1 = last_contact - first_contact
delta_2 = datetime.now() - last_visit
delta_3 = datetime.now() - last_contact

st.header('Numeri importanti')

col1, col2, col3 = st.columns(3)

col1.metric("Da quanti giorni ci sentiamo 💕", delta_1.days)
col2.metric("Da quanti giorni non ci vediamo 😢", delta_2.days)
col3.metric("Da quanti giorni non ci sentiamo 😔", delta_3.days)

st.header('Statistiche importanti')

st.write("Messaggi scambiati nel tempo")
fig = px.histogram(df, x="data", y="count_messaggi", nbins=df.shape[0])
st.plotly_chart(fig, use_container_width=True)

st.write("Ti amo scambiati nel tempo")
fig = px.histogram(df, x="data", y="count_ti_amo", nbins=df.shape[0])
st.plotly_chart(fig, use_container_width=True)

st.write("Incontri nel tempo")
fig = px.histogram(df, x="data", y="visti", nbins=df.shape[0])
st.plotly_chart(fig, use_container_width=True)
