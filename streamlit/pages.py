import pandas as pd
import streamlit as st
import pg_show_category_products
import pg_search_product
import pg_about
import pg_user_prefs
import pg_homepage
import pg_test
from Src.utils import *

st.set_page_config(
    page_title="Safe Food For Everyone",
    page_icon="path_of_your_favicon",
    layout="wide",
    initial_sidebar_state="auto",
)

def main():
    local_css("style.css")
    st.header("Safe Food for Everyone")
    if (st.sidebar.button("User Preferences",type="secondary")):
        pg_user_prefs.app()
    if (st.sidebar.button("Search Product",type="secondary")):
        pg_search_product.app()
    category_df = read_categories_data()
    category_df = pd.read_csv('Datasets/df_cat.csv', sep=';', low_memory=False)
    buttons = []
    category_list = category_df["Name"].values
    for col in category_list:
        buttons.append((col, st.sidebar.button(col, type="primary")))
    for cat, button in buttons:
        if button:
            pg_show_category_products.app(cat)
    if (st.sidebar.button("About", type="secondary")):
        pg_about.app()
    if ("current_page" in st.session_state):
        if (st.session_state.current_page == "pg_homepage"):
            pg_homepage.app()
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def app():
    st.markdown("Welcome to the home page")

if __name__ ==  "__main__":
     main()