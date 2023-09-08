import pandas as pd

def read_food_data():
    df = pd.read_csv('Datasets/df.csv', sep=';', low_memory=False)
    df["GI_category"] = 1
    return df

    def read_food_data2():
        df = pd.read_csv('Datasets/df.csv', sep=';', low_memory=False)
        df["GI_category"] = 1
        return df

def read_categories_data():
    df = pd.read_csv('Datasets/df_cat.csv', sep=';', low_memory=False)
    return df

