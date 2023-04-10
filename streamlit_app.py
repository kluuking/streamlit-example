from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image
import csv
# Import writer class from csv module
from csv import writer
 



"""
# Welcome to ShopWise    
Please select  the food item and the ammount you would like to buy ShopWise will provide some details of the recommended amount. 
"""
# Display the Logo- Start---- -
image = Image.open('Shopwise_Logo.png')

st.image(image, caption='Shop Wisely')

#----- END ------- 

#---- Select Box for picking the item in question - Start 
option = st.selectbox(
     'What item would you like to buy',
    ('Apple', 'Beef', 'Milk'))

st.write('You selected:', option)

#---- Select Box for picking the item in question - End 

# ---- Basic informing user what they selected tied back to a user's recommended value- Start 

with st.echo(code_location='below'):
     Purchase_Ammount = st.slider("How many do you want to buy", 1, 10, 1) 
     recommended_apple_ammount = 6 
     if Purchase_Ammount > recommended_apple_ammount:
          st.write('we recommened you buy' , recommended_apple_ammount, option, 'Not', Purchase_Ammount) 
     if Purchase_Ammount < recommended_apple_ammount:
          st.write('You want to buy', option, Purchase_Ammount)
          
# ---- Basic informing user what they selected tied back to a user's recommended value-  End 
"""
#For Testing this adds Grapes with 30 Experation and 70 CO2 
"""
if st.button('Press to add Grapes'):
    st.write('The Item/s have been added')
# List that we want to add as a new row
    List = ["Grapes", '30', "70"]
 
# Open our existing CSV file in append mode
# Create a file object for this file
    with open('StreamLIST Sheet test.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()

else:
     st.write('Dont press unless you are sure')
     
#Read in CSV from Github Files 
if st.button('Press to see the updated CSV' ):
     data = pd.read_csv("StreamLIST Sheet test.csv") #path folder of the data file
     st.write(data) #displays the table of data
   #Kevin F's Google sheet connection 
   
   
# Connect to the Google Sheet
sheet_id = "1X5ANn3c5UKfpc-P20sMRLJhHggeSaclVfXavdfv-X1c"
sheet_name = "Food_List_Master"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url, dtype=str).fillna("")

df

# Build a user interface and search functionality
text_search = st.text_input("Search items by item description", value="")

m1 = df["Name"].str.contains(text_search)
m2 = df["Catagory"].str.contains(text_search)
df_search = df[m1 | m2]

if text_search:
    st.write(df_search)



