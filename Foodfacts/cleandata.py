git clone https://github.com/cemregur/QueensOfData.git
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)

# Data import starts here!
# Biscuits and cakes
df1 = pd.read_csv("openfoodfacts_export _biscuits_cakes.csv",delimiter="\t", low_memory=False)

# Category_new variable was added each dataframe
df1["Category_new"] = "biscuits_and_cakes"

# Select common lc such as "en"
df1 = df1[df1["lc"] == "en"]

#selected_columns = [col for col in df1.columns if col.startswith(("product", "generic"))]
#df1 = df1.drop(columns = selected_columns)
#df1.columns

# Chips (Doritos) category
df2 = pd.read_csv("openfoodfacts_export _doritos.csv",delimiter="\t", low_memory=False)
df2["Category_new"] = "Chips"
df2 = df2[df2["lc"] == "en"]
#selected_columns = [col for col in df2.columns if col.startswith(("product", "generic"))]
#df2 = df2.drop(columns = selected_columns)
#df2.columns
# Chocolate (kinder) category
df3 = pd.read_csv("openfoodfacts_export _kinder.csv",delimiter="\t", low_memory=False)
df3["Category_new"] = "chocolate"
df3 = df3[df3["lc"] == "en"]

# Chips (lays) category
df4 = pd.read_csv("openfoodfacts_export _lays.csv",delimiter="\t", low_memory=False)
df4["Category_new"] = "chips"
df4 = df4[df4["lc"] == "en"]

# Chocolate (milka) category
df5 = pd.read_csv("openfoodfacts_export _milka.csv",delimiter="\t", low_memory=False)
df5["Category_new"] = "chocolate"
df5 = df5[df5["lc"] == "en"]

# Chocolate (nesquik) category
df6 = pd.read_csv("openfoodfacts_export _nesquik.csv",delimiter="\t", low_memory=False)
df6["Category_new"] = "chocolate"
df6 = df6[df6["lc"] == "en"]

# Chocolate (nutella) category
df7 = pd.read_csv("openfoodfacts_export _nutella.csv",delimiter="\t", low_memory=False)
df7["Category_new"] = "chocolate"
df7 = df7[df7["lc"] == "en"]

# Baby_food category
df8 = pd.read_csv("openfoodfacts_export_bebek_mamasi.csv",delimiter="\t", low_memory=False)
df8["Category_new"] = "baby_food"
df8 = df8[df8["lc"] == "en"]

# Cereal category
df9 = pd.read_csv("openfoodfacts_export_cereal.csv",delimiter="\t", low_memory=False)
df9["Category_new"] = "cereal"
df9 = df9[df9["lc"] == "en"]

# Chocolate (danone) category
df10 = pd.read_csv("openfoodfacts_export_danone.csv",delimiter="\t", low_memory=False)
df10["Category_new"] = "chocolate"
df10 = df10[df10["lc"] == "en"]

# Frozen food category
df11 = pd.read_csv("openfoodfacts_export_frozen_food.csv",delimiter="\t", low_memory=False)
df11["Category_new"] = "frozen_food"
df11 = df11[df11["lc"] == "en"]

# Fruit juice category
df12 = pd.read_csv("openfoodfacts_export_fruit_juice.csv",delimiter="\t", low_memory=False)
df12["Category_new"] = "fruit_juice"
df12 = df12[df12["lc"] == "en"]

# Pasta category
df13 = pd.read_csv("openfoodfacts_export_pasta.csv",delimiter="\t", low_memory=False)
df13["Category_new"] = "pasta"
df13 = df13[df13["lc"] == "en"]

# Chips (pringles) category
df14 = pd.read_csv("openfoodfacts_export_pringles.csv",delimiter="\t", low_memory=False)
df14["Category_new"] = "chips"
df14 = df14[df14["lc"] == "en"]

# Yogurt category
df15 = pd.read_csv("openfoodfacts_export_yogurt.csv", delimiter="\t", low_memory=False)
df15["Category_new"] = "yogurt"
df15 = df15[df15["lc"] == "en"]

# Data set list
veri_seti = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15]

# Combine all dataframe [df1:df15]
yeni_df = pd.concat(veri_seti, ignore_index=True, sort=False)

yeni_df.head(30)

yeni_df["Category_new"].unique()
yeni_df["off:nutriscore_grade"].values.count()
yeni_df.head()
yeni_df["off:nutriscore_score"].head()
yeni_df["off:nutriscore_score"].isnull().mean() * 100

yeni_df.dropna(subset=["off:nutriscore_score"], inplace=True)
yeni_df.to_excel("son_data.xlsx", index=False)


# selected_columns = [col for col in df15.columns if col.startswith(("ingredients"))]

# Determination of common columns starts here!

# Common columns
ortak_sutunlar = set(veri_seti[0].columns)

for df in veri_seti[1:]:
    ortak_sutunlar &= set(df.columns)
df.head(10)

my_list = list(ortak_sutunlar)

#df_set = pd.DataFrame(my_list, columns=["MyColumn"])
#df_set.to_excel("kume_verisi.xlsx", index=False)

# New data frame
yeni_df = pd.concat([df[my_list] for df in veri_seti], ignore_index=False)

#new dataframe exports as csv file
yeni_df.to_csv("df_new.csv", sep=";",index=False, decimal=",")

# Calculation of missing value percentage
missing_percentage = yeni_df.isnull().mean() * 100
missing_percentage_sorted = missing_percentage.sort_values(ascending=False)

type(missing_percentage)
missing_percentage_sorted.to_csv("kayıp_gozlem.csv",sep=";", index = False)

plt.figure(figsize=(20, 10))
sns.barplot(x=missing_percentage_sorted.values, y=missing_percentage_sorted.index)
plt.title('Eksik Veri Yüzdesi')
plt.xlabel('Sütunlar')
plt.ylabel('Eksik Veri Yüzdesi (%)')
plt.xticks(rotation=45)
plt.show(block=True)

