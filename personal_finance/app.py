import ui
import streamlit as st
import json


app_data = json.load(open("data/app_config.json"))
app = st.title(app_data['title'])
ui.show_fire()