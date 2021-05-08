import streamlit as st
import pandas as pd
from nlp import metadata_search_engine
from mba import product_recommender
st.title('Instacart')

st.write("Please login using your User ID")
user_id = st.text_input("User ID:", 00000)
if user_id.isdigit() == False:
    st.write("**Please enter a valid User ID**")
user_id = int(user_id)
st.write("Product Search Engine")
product_name = st.text_input("Product Search:", "")
prod = []

df = metadata_search_engine(product_name)
dict1 = df.to_dict()
option = st.selectbox("Search results", list(dict1.items()), 0, format_func=lambda o: o[1])
prod.append(option[1])


results = product_recommender(user_id, prod[0], 1, 5)
res_df = pd.DataFrame(results, columns=['Recommended Products'])
st.dataframe(res_df)










