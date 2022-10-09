
# import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

url = "https://data.mongodb-api.com/app/data-eajpu/endpoint/data/v1/action/findOne"

# st.title('New Scouting App')



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
    