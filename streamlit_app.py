import streamlit

streamlit.title('my parents new healthy dinner')

streamlit.header('breakfast menu')
streamlit.text(' 🥣 omega 3 & blueberry oatmeal ')
streamlit.text(' 🥗 kale, spinach & rocket smoothie ')
streamlit.text(' 🐔 hard-boiled free-range egg')
streamlit.text(' 🥑🍞 avokado thost ')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

