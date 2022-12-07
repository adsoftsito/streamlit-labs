import json
import numpy as np
import requests
import streamlit as st 

# The server URL specifies the endpoint of your server running the linear_model
# model with the name "linear_model" and using the predict interface.
SERVER_URL = 'https://linear-model-service-adsoftsito.cloud.okteto.net/v1/models/linear-model:predict'
 
def callApi():
  predict_request = '{"instances" : [ [20.0], [25.0], [30.0], [35.0] ]}'
 
  # Send few actual requests and report average latency.
  total_time = 0
  num_requests = 10
  index = 0
  for _ in range(num_requests):
    response = requests.post(SERVER_URL, data=predict_request)
    response.raise_for_status()
    total_time += response.elapsed.total_seconds()
    prediction = response.json()
    st.write (prediction)
 
st.title('Api demo')
myapi = st.button('Call Api')

if myapi:
    callApi()

