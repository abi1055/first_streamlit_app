import streamlit
import pandas
import numpy 

streamlit.title('My Parents New Healthy Diner Menu')
streamlit.header('🍞 Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits = fruits.set_index('Fruit')

#lets put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick Some Fruits:", list(fruits.index), ['Avocado', 'Strawberries'])
fruits_to_show = fruits.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

#New Section to display api fruityvise response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json()) #just writes the data to the screen

# take the json version of the response and normalize it (so it is readable on the app)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# making response into a dataframe (again organizes better on app)
streamlit.dataframe(fruityvice_normalized)

