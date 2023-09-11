import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from Src.utils import *

def app():
    st.write("test page")
    df = read_food_data()
    cols = ["code", "product_name_en", "brands", "off:nova_groups", "off:nutriscore_grade", "url"]
    df = df.loc[df["Category_new"] == "Pasta", cols]
    grd = GridOptionsBuilder.from_dataframe(df)
    grd.configure_pagination(enabled=True)
    grd.configure_default_column(groupable=True)
    gridOptions = grd.build()

    grd_Table = AgGrid(df,
                       gridOptions=gridOptions,
                       fit_columns_on_grid_load=True,
                       height=500,
                       width="100%",
                       theme = "streamlit",
                       reload_data=True,
                       update_mode= GridUpdateMode.GRID_CHANGED,
                       allow_unsafe_jscode=True,
                       editible = True
                       )
    st.write(grd_Table)
    st.write("Merhaba")