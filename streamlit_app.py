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

#Pick alist here, customer can pick the fruit
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#diplay the table on the page
streamlit.dataframe(my_fruit_list)

