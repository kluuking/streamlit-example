from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image
import csv



"""
# Welcome to ShopWise    

Please select  the food item you would like to buy and ammount when the ammount is selected it will provide some details of the recommended amount. 

"""
image = Image.open('Shopwise_Logo.png')

st.image(image, caption='Shop Wisely')

option = st.selectbox(
     'What item would you like to buy',
    ('Apple', 'Beef', 'Milk'))

st.write('You selected:', option)

with st.echo(code_location='below'):
     Purchase_Ammount = st.slider("How many do you want to buy", 1, 10, 1) 
     recommended_apple_ammount = 6 
     if Purchase_Ammount > recommended_apple_ammount:
          st.write('we recommened you buy' , recommended_apple_ammount, option, 'Not', Purchase_Ammount) 
     if Purchase_Ammount < recommended_apple_ammount:
          st.write('You want to buy', option, Purchase_Ammount)

if st.button('Press to add to CSV'):
    st.write('The Item/s have been added')
    # open the file in the write mode
    f = open('StreamLIST Sheet test.csv', 'w')
    # create the csv writer
    writer = csv.writer(f)
    # write a row to the csv file
    writer.writerow([bannna, 1, 3])
    # close the file
    f.close()



     
          
#Read in CSV from Github Files 

data = pd.read_csv("StreamLIST Sheet test.csv") #path folder of the data file
st.write(data) #displays the table of data
     
# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url,error_bad_lines=False)

df = load_data(st.secrets["public_gsheets_url"])

df

# Print results.
#for row in df.itertuples():
    #st.write(f"{row.name} has a :{row.pet}:")
          
