from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

This is a placeholder 

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

option = st.selectbox(
     'How would you like to be contacted?',
    ('Apple', 'Beef', 'Milk'))

st.write('You selected:', option)

with st.echo(code_location='below'):
     Purchase_Ammount = st.slider("How many do you want to buy", 1, 10, 1) 
     st.write('You want to buy', option, Purchase_Ammount)
     
# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url,error_bad_lines=False)

df = load_data(st.secrets["public_gsheets_url"])

print(df)

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
          
