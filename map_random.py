import streamlit as st 
import pandas as pd
import numpy as np

map_data = pd.DataFrame(

  np.random.randn(100, 2) / [50, 50] + [25.67507, -100.31847],
  columns=['latitude', 'longitude']

  )
st.dataframe(map_data)

st.map(map_data)