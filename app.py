# import libraries
import os
import google.generativeai as genai
import streamlit as st
import datetime

# configure key
# use the environment variable GOOGLE_API_KEY for api access
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Title
st.title('AI Travel Planner')

# Subtitle
st.subheader('Plan your next trip with AI')

# Sidebar
st.sidebar.header('Enter details to generate a travel plan:')

# get google api key from the user but don't display it
api_key = st.sidebar.text_input('Enter Your Google API Key')

# source, destination, date, budget, duration
source = st.sidebar.text_input('Source', 'New York')
destination = st.sidebar.text_input('Destination', 'Los Angeles')
date = st.sidebar.date_input('Travel Start Date', "today").strftime('%Y-%m-%d')
budget = st.sidebar.number_input('Budget', 1000)
duration = st.sidebar.slider('Duration', 1, 90, 5)

def get_the_planner(message, api_key):
  # get model
  genai.configure(api_key=api_key)
  model = genai.GenerativeModel('gemini-pro')
  response = model.generate_content(message)
  return response.text

# create a message to send to the model using the user input
message = f"Plan a trip from {source} to {destination} on {date} with a budget of ${budget} for {duration} days."


# display the response when clicked on button
if st.sidebar.button('Generate Travel Plan'):
    # generate travel plan if all fields are filled else display error message
    if api_key and source and destination and date and budget and duration:
        # show message till get response 
        with st.spinner('Generating Travel Plan...'):
            response = get_the_planner(message, api_key)
        st.success('Here is your generated travel plan:')
        st.markdown(response)
    else:
        st.error('Please fill in all the fields to generate the travel plan.')
