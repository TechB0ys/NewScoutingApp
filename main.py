
import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

url = "https://data.mongodb-api.com/app/data-eajpu/endpoint/data/v1/action/findOne"

payload = json.dumps({
  "collection": "testData",
  "database": "Cluster0",
  "dataSource": "Cluster0",
  "projection": {}
})

headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': "ZtQO9OKBe8v5QSliNgjP7vdCzzZBU0OBTOfsvlc6EidIbvwp5LLAYBvPJVHhwcvR", 
}


@st.cache
def load_data():
  data = requests.request("POST", url, headers=headers, data=payload)
  return data.json()
    
def main_page():
  st.markdown("# Main page 🎈")
  st.sidebar.markdown("# Main page 🎈")

def page2():
  st.markdown("# Page 2 ❄️")
  st.sidebar.markdown("# Page 2 ❄️")

page_names_to_funcs = {
  "Main Page": main_page,
  "Page 2": page2
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()    
    
    
# TODO
# Title: 2022-2023 Scout App
# Sidebar
# Main page make datavisual
# Page 2 is input and change name
