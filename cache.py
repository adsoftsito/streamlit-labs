import streamlit as st
import pandas as pd 

st.title("Streamlit con cache")

#DATA_URL = 'https://raw.githubusercontent.com/adsoftsito/streamlit-labs/master/dataset.csv?token=GHSAT0AAAAAAB2NR7KYLAP4VXUGLOVWKVL6Y3NHLEQ'
DATA_URL =  'https://raw.githubusercontent.com/AngelCavazos/streamlit-labs/master/dataset.csv?token=GHSAT0AAAAAAB2XYZDNMM6IXFT5C2TPCA7UY3NFUYQ'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Loading data ...')
data = load_data(90000)
data_load_state.text("Done ...")

st.dataframe(data)
