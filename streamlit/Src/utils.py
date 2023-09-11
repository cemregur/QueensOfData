import pandas as pd
from pandas import DataFrame

def read_food_data():
    df = pd.read_csv('Datasets/df.csv', sep=';', low_memory=False)
    df["off:nova_groups"] = df["off:nova_groups"].apply(lambda x: int(float(x.split()[0].replace(',', '.'))))
    #df["GI_category"] = 1
    df = df.fillna("")
    return df

    return df

def read_food_data2():
    df = pd.read_csv('Datasets/df.csv', sep=';', low_memory=False)
    df["off:nova_groups"] = df["off:nova_groups"].apply(lambda x: int(float(x.split()[0].replace(',', '.'))))
    #df["GI_category"] = 1
    df = df.fillna("")
    return df

def read_categories_data():
    df = pd.read_csv('Datasets/df_cat.csv', sep=';', low_memory=False)
    return df

