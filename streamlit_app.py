import streamlit 
import pandas
import snowflake.connector
import requests

from urllib.error import URLError

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
try:
  
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)
      
except URLError as e:
  streamlit.error()

  
  
streamlit.stop()



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


add_my_fruit = streamlit.text_input('What fruit would you like add?','jackfruit')
streamlit.write('Thanks for adding ', add_my_fruit)


#Thisi will not work
my_cur.execute("INSERT INTO fruit_load_list values ('from streamlit')")

