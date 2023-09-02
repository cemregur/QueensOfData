
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
df1 = pd.read_csv("openfoodfacts_export _biscuits_cakes.csv",delimiter="\t", low_memory=False)
#selected_columns = [col for col in df1.columns if col.startswith(("product", "generic"))]
#df1 = df1.drop(columns = selected_columns)
#df1.columns
df2 = pd.read_csv("openfoodfacts_export _doritos.csv",delimiter="\t", low_memory=False)
#selected_columns = [col for col in df2.columns if col.startswith(("product", "generic"))]
#df2 = df2.drop(columns = selected_columns)
#df2.columns
df3 = pd.read_csv("openfoodfacts_export _kinder.csv",delimiter="\t", low_memory=False)
df4 = pd.read_csv("openfoodfacts_export _lays.csv",delimiter="\t", low_memory=False)
df5 = pd.read_csv("openfoodfacts_export _milka.csv",delimiter="\t", low_memory=False)
df6 = pd.read_csv("openfoodfacts_export _nesquik.csv",delimiter="\t", low_memory=False)
df7 = pd.read_csv("openfoodfacts_export _nutella.csv",delimiter="\t", low_memory=False)
df8 = pd.read_csv("openfoodfacts_export_bebek_mamasi.csv",delimiter="\t", low_memory=False)
df9 = pd.read_csv("openfoodfacts_export_cereal.csv",delimiter="\t", low_memory=False)
df10 = pd.read_csv("openfoodfacts_export_danone.csv",delimiter="\t", low_memory=False)
df11 = pd.read_csv("openfoodfacts_export_frozen_food.csv",delimiter="\t", low_memory=False)
df12 = pd.read_csv("openfoodfacts_export_fruit_juice.csv",delimiter="\t", low_memory=False)
df13 = pd.read_csv("openfoodfacts_export_pasta.csv",delimiter="\t", low_memory=False)
df14 = pd.read_csv("openfoodfacts_export_pringles.csv",delimiter="\t", low_memory=False)
df15 = pd.read_csv("openfoodfacts_export_yogurt.csv", delimiter="\t", low_memory=False)

# Ortak sütunların belirlenmesi

veri_setleri = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15]

# Ortak sütunlar
ortak_sutunlar = set(veri_setleri[0].columns)

for df in veri_setleri[1:]:
    ortak_sutunlar &= set(df.columns)

# Yeni data frame
yeni_df = pd.concat([df[ortak_sutunlar] for df in veri_setleri], ignore_index=True)

print(yeni_df.head())

yeni_df.to_excel("yeni_veri.xlsx", index=False)

missing_percentage = yeni_df.isnull().mean() * 100
missing_percentage_sorted = missing_percentage.sort_values(ascending=False)

plt.figure(figsize=(20, 10))
sns.barplot(x=missing_percentage_sorted.values, y=missing_percentage_sorted.index)
plt.title('Eksik Veri Yüzdesi')
plt.xlabel('Sütunlar')
plt.ylabel('Eksik Veri Yüzdesi (%)')
plt.xticks(rotation=45)
plt.show(block=True)

