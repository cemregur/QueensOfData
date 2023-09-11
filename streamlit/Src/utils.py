import pandas as pd
from pandas import DataFrame


def read_food_data():
    df = pd.read_csv('streamlit/Datasets/df.csv', sep=';', low_memory=False)
    return df


def read_food_data2():
    df = pd.read_csv('streamlit/Datasets/df.csv', sep=';', low_memory=False)
    return df


def read_categories_data():
    df = pd.read_csv('streamlit/Datasets/df_cat.csv', sep=';', low_memory=False)
    return df
