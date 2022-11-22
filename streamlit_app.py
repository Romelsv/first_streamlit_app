import streamlit 
import pandas

streamlit.title('My parents New healty Diner')


streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado and Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


#Pick alist here, customer can pick the fruit
fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruit_to_show=my_fruit_list.loc[fruit_selected]

#diplay the table on the page
streamlit.dataframe(fruit_to_show)


streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")

# convert json to dict
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# put them in a pandas dataframe
streamlit.dataframe(fruityvice_normalized)
