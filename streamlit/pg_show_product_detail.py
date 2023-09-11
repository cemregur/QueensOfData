import streamlit as st
import pandas as pd
from Src.utils import *

def show_Product_Detail(xproduct_code):
    df = get_product_detail_df(xproduct_code)
    if (df.shape[0] != 1):
        st.error("An error occured with the product code :" + str(xproduct_code))
    else:
        col1, col2 = st.columns((1,2))
        col1.image(df["url"].values[0], caption='', use_column_width=True)
        col2.header(df["product_name_en"].values[0])
        col2.markdown("Code : " + str(df["code"].values[0]))
        col2.markdown("Ingredients : " + df["ingredients_text_en"].values[0])
        col2.markdown("Brands : " + df["brands"].values[0])
        if (str(df["stores"].values[0]) != ""):
            col2.markdown("Stores : " + df["stores"].values[0])
        else:
            col2.markdown("Stores : ...")
        col2.markdown("Allergens : " + df["allergens"].values[0])
        ########################################################################
        # SCORES
        ########################################################################
        with st.container():
            col1 , col2, col3  = st.columns(3)
            col1.success("Nutrition Score : " + df["off:nutriscore_grade"].values[0] )
            col2.error('NOVA Score : ' + df["off:nova_groups"].values[0], icon="🚨")
            #col3.success("Glisemic Score : " + str(df["GI_category"].values[0]))
        #######################################################################
        # ALLERGENS
        ########################################################################
        Allergen_Count = 0
        Allergen_Pozitives_list = []
        Allergen_col_list = [col for col in df.columns if "Allergen" in col]
        for col in Allergen_col_list:
            if str(df[col].values[0]) == "1":
                Allergen_Pozitives_list.append(col)
        Allergen_Count = len(Allergen_Pozitives_list)
        if Allergen_Count > 0:
            col_obj_list = st.columns(Allergen_Count)
            for i, col_object in enumerate(col_obj_list):
                col_object.error(Allergen_Pozitives_list[i] + " POZITIVE ALARM" , icon="🚨" )
        if Allergen_Count == 0:
            # Allerjen bilgisi girilmedi
            if (df["Allergen_Milk"].values[0] == "2"):
                col_obj_list = st.columns(6)
                for i, col_object in enumerate(col_obj_list):
                    col_object.info(Allergen_col_list[i] + " No Information")

def check_allergens(df_product ):
    if (df_product["allergens"].values[0] == ""):
        allergens = []
        df_product["Allergen_Milk"] = "2"
        df_product["Allergen_Egg"] = "2"
        df_product["Allergen_Nut"] = "2"
        df_product["Allergen_Peanut"] = "2"
        df_product["Allergen_Gluten"] = "2"
        df_product["Allergen_Soybeans"] = "2"
        return df_product
    else:
        allergens = df_product["allergens"].values[0].split(", ")
        chk = True
        df_product["Allergen_Milk"] = "0"
        if ("pref_Allergen_Milk" in st.session_state):
            if (st.session_state.pref_Allergen_Milk == 0):
                chk = False
        if (chk) & ("Milk" in allergens):
            df_product["Allergen_Milk"] = "1"
        chk = True
        df_product["Allergen_Gluten"] = "0"
        if ("pref_Allergen_Gluten" in st.session_state):
            if (st.session_state.pref_Allergen_Gluten == 0):
                chk = False
        if (chk) & ("Gluten" in allergens):
            df_product["Allergen_Gluten"] = "1"
        df_product["Allergen_Egg"] = "0"
        if ("pref_Allergen_Egg" in st.session_state):
            if (st.session_state.pref_Allergen_Egg == 0):
                chk = False
        if (chk) & ("Egg" in allergens):
            df_product["Allergen_Egg"] = "1"
        df_product["Allergen_Nut"] = "0"
        if ("pref_Allergen_Nut" in st.session_state):
            if (st.session_state.pref_Allergen_Nut == 0):
                chk = False
        if (chk) & ("Nut" in allergens):
            df_product["Allergen_Nut"] = "1"
        df_product["Allergen_Peanut"] = "0"
        if ("pref_Allergen_Peanut" in st.session_state):
            if (st.session_state.pref_Allergen_Peanut == 0):
                chk = False
        if (chk) & ("Peanut" in allergens):
            df_product["Allergen_Peanut"] = "1"
        df_product["Allergen_Soybeans"] = "0"
        if ("pref_Allergen_Soybeans" in st.session_state):
            if (st.session_state.pref_Allergen_Soybeans == 0):
                chk = False
        if (chk) & ("Soybeans" in allergens):
            df_product["Allergen_Soybeans"] = "1"
        return df_product
def get_product_detail_df(xproduct_code):
    #df = read_food_data2()
    df = pd.read_csv('Datasets/df.csv', sep=';', low_memory=False)
    df.loc[df["allergens"].isnull(), "allergens"] = ""
    df.loc[df["stores"].isnull(), "stores"] = ""
    df["GI_category"] = 1

    cols = ["code", "product_name_en", "brands", "off:nova_groups", "off:nutriscore_grade", "allergens",
            "ingredients_text_en", "stores", "url"]
    df_product = df.loc[df["code"].astype(str) == str(xproduct_code), cols]
    df_product_detail = check_allergens(df_product)
    return df_product_detail

def app(xproduct_code):
    show_Product_Detail(xproduct_code)