import pandas as pd
import streamlit as st
import food_fact_app

df = pd.read_csv("streamlit/Datasets/df.csv", low_memory=False)

df.head()
df.columns()


# Glisemik indeksi hesapla
def calculate_glycemic_index(row):
    carbohydrates = row['carbohydrates_value']
    fiber = row['fiber_value']
    sugars = row['sugars_value']
    proteins = row['proteins_value']
    fats = row['fat_value']

    glycemic_index = (carbohydrates - fiber + 0.1 * sugars + 0.15 * proteins + 0.1 * fats)
    return glycemic_index


# Glisemik indeks sütununu hesapla ve DataFrame'e ekle
df['glycemic_index'] = df.apply(calculate_glycemic_index, axis=1)
print(df)
df.head()

# Literatürde Glisemik indekslerine göre gıdalar
# düşük (1-55), orta (56-69) ve yüksek (>70) Gİ’li olarak sınıflandırılır.

# Kategorik bir sütun oluşturun
df['GI_category'] = pd.cut(df['glycemic_index'], bins=[0, 55, 69, float('inf')],
                           labels=['low_gi', 'medium_gi', 'high_gi'], right=False)

print(df)
