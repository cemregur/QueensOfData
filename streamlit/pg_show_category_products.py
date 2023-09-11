import streamlit as st
import pandas as pd
from Src.utils import *
def get_category_product_list(xCategory):
    df = read_food_data()
        ##BAK
    cols = ["code", "product_name_en", "brands", "off:nova_groups", "off:nutriscore_grade", "url"]
    df = df.loc[df["Category_new"] == xCategory, cols]

    return df

def show_product_list(df):
    try:
        st.table(df)
    except:
        st.error("Something went wrong when getting products")
    finally:
        st.write("Finally")
def app(xCategory = ""):
    if (xCategory != ""):
        df = get_category_product_list(xCategory)
        show_product_list(df)
    else:
        st.error("No defined Category")