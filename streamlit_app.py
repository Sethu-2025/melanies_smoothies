# Import python packages
pip install streamlit snowflake-connector-python snowflake-snowpark-python
import streamlit as st
from snowflake.snowpark.functions import col
# Write directly to the app
st.title(":cup_with_straw: Customize your Smoothie: :cup_with_straw:")
st.write(
  """Choose the fruits you want in your customize smoothie
  """ 
)

name_on_order = st.text_input("Name on Smoothie")
st.write("The name of smoothie will be", name_on_order)
cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
st.dataframe(data=my_dataframe, use_container_width=True)

import streamlit as st

ingredients_list = st.multiselect("Choose up to 5 ingredients:",
my_dataframe, max_selections=5
)

if ingredients_list:
 Ingredients_string =''
 for fruit_chosen in ingredients_list:
     Ingredients_string += fruit_chosen + ' '
     #st.write(Ingredients_string)
     
my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + Ingredients_string + """','""" + name_on_order + """')"""

#st.write(my_insert_stmt)
#st.stop()
time_to_insert = st.button('Submit Order')
if time_to_insert:
    session.sql(my_insert_stmt).collect()
    st.success('Your Smoothie is ordered!', icon="✅")
