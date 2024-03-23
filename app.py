# import libraries
import os
import google.generativeai as genai
import streamlit as st
import datetime

# configure key
# use the environment variable GOOGLE_API_KEY for api access
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Title
st.title('AI Travel Planner')

# Subtitle
st.subheader('Plan your next trip with AI')

# Sidebar
st.sidebar.header('User Input Parameters')
# source, destination, date, budget, duration
source = st.sidebar.text_input('Source', 'New York')
destination = st.sidebar.text_input('Destination', 'Los Angeles')
date = st.sidebar.date_input('Travel Start Date', datetime.date(2021, 1, 1)).strftime('%Y-%m-%d')
budget = st.sidebar.number_input('Budget', 1000)
duration = st.sidebar.slider('Duration', 1, 10, 5)

def get_the_planner(message):
  # get model
  model = genai.GenerativeModel('gemini-pro')
  chat = model.start_chat()

  response = chat.send_message(message)
  return response.text

# create a message to send to the model using the user input
message = f"Plan a trip from {source} to {destination} on {date} with a budget of ${budget} for {duration} days."

# get the response from the model
response = get_the_planner(message)

# display the response
st.write(response)

