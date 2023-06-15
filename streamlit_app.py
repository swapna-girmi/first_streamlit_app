import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('my parents new healthy dinner')

streamlit.header('breakfast menu')
streamlit.text(' 🥣 omega 3 & blueberry oatmeal ')
streamlit.text(' 🥗 kale, spinach & rocket smoothie ')
streamlit.text(' 🐔 hard-boiled free-range egg')
streamlit.text(' 🥑🍞 avokado thost ')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_selected )


# # create a function(repeatable code block)
# def get_fruityvice_data(this_fruit_choice):
#         fruityvice_responce = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
#         fruityvice_normalized = pandas.json_normalize(fruityvice_responce.json())
#         return fruityvice_normalized
# # Display the table on the page.
# streamlit.header('Fruityvice Fruit Advice!')
# try:
#     fruit_choice = streamlit.text_input('What fruit would you like information about?')
#     if not fruit_choice:
#         streamlit.error("please select a fruit to get inforamtion about.")
#     else:
#         back_from_function = get_fruityvice_data(fruit_choice)
#         streamlit.dataframe(back_from_function)
#         #fruityvice_responce = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#         #fruityvice_normalized = pandas.json_normalize(fruityvice_responce.json())
#         #streamlit.dataframe(fruityvice_normalized)
# except URLError as e:
#     streamlit.error()


# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)


# # write your own comment -what does the next line do? 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# # write your own comment - what does this do?
# streamlit.dataframe(fruityvice_normalized)

streamlit.header("The fruit load list contains:")
#snowflake-related functions
# def get_fruit_load_list():
#         with my_cnx.cursor() as my_cur:
#              my_cur.execute("select * from fruit_load_list")
#              return my_cur.fetchall()
# #add a buttom to load the fruit
# if streamlit.button('Get Fruit Load List'):
#       my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#       my_data_rows = get_fruit_load_list()
#       streamlit.dataframe(my_data_rows)

#allow the end user to add a fruit to the list
list=['jackfruit', 'papaya', 'guava', 'kiwi']
def insert_row_snowflake(new_fruit):
        with my_cnx.cursor() as my_cur:
                #my_cur.executemany("insert into fruit_load_list values('jackfruit', 'papaya', 'guava' ,'kiwi')")
                my_cur.executemany('insert into fruit_load_list values (?)', 
                   [(n,) for n in list])
                return "Thanks for adding " + new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
         my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
         back_from_function = insert_row_snowflake(add_my_fruit)
         streamlit.text(back_from_function)
                

        
# #import 
# my_cur = my_cnx.cursor()
# my_cur.execute("select * from fruit_load_list")snowflake.connector
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_data_rows = my_cur.fetchall()
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_rows)

# #add_my_fruit = streamlit.text_input('what fruit would you like to add?','jackfruit')
# #streamlit.write('Thanks for adding jackfruit ', add_my_fruit)



  


 

