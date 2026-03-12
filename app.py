import streamlit as st
from db_operations import data_ready

df_app,df_rev,df_gen,df_appgen = data_ready()

st.success("Veriler hafızaya yüklendi")