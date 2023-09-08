import streamlit as st
import pandas as pd
import pg_show_category_products
import pg_show_product_detail
from Src.utils import *

def search_product():
    search_text = st.session_state.txt_search
    df = read_food_data()
    ##BAK hangi sütunlar çekilecekse loca liste gönderilmeli.
    cols = ["code", "product_name_en", "brands", "off:nova_groups", "off:nutriscore_grade", "GI_category", "url"]
    result_df = df.loc[(df["product_name_en"].str.contains(search_text)) |
                       (df["code"].astype(str).str.contains(search_text)), cols]
    ## if the result set contains only one product
    if (result_df.shape[0] == 0):
        st.session_state.notfound = "There is not any food product with " + search_text
        app()
    elif (result_df.shape[0] == 1):
        product_code = result_df["code"].values[0]
        pg_show_product_detail.app(product_code)
    else:
        pg_show_category_products.show_product_list(result_df)

def show_Product_Search_Form():
    with st.form(key="product_search_form"):
        st.text_input(label="Product", key="txt_search")
        st.form_submit_button(label="Search",on_click=search_product)
    if ("notfound" in st.session_state):
        if (st.session_state.notfound != ""):
            st.info(st.session_state.notfound)
            st.session_state.notfound = ""

def app():
    show_Product_Search_Form()