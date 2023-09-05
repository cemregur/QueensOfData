import pandas as pd
import streamlit as st

import food_fact_app

df_ = pd.read_excel("/Users/cemregur/QueensOfData/finalProject/new_spagetti.xlsx")
df = df_.copy()

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

# user_preferences

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)



# Streamlit uygulamasını oluşturun
st.set_page_config(
    page_title="Safety Food For Everyone",
    page_icon="path_of_your_favicon",
    layout="wide",
    initial_sidebar_state="auto",
)
st.title("Food Fact Application")

# Adım 1: Kategori seçimi
st.subheader("Step 1: Select Product Category")
selected_category = st.selectbox("Select Product Category", df["categories"].unique())

# Adım 2: Tercihler için başka bir sayfaya git
if st.button("Edit Preferences"):
    st.write(f"Selected Category: {selected_category}")
    st.write("You are being redirected to the next page for preferences...")
    st.write("Please specify your preferences.")
    st.write("---")

    # Adım 3: Tercihler
    st.subheader("Adım 2: Preferences")

    # Kullanıcının tercihlerini alın
    st.sidebar.title("Preferences")
    nutritional_quality = st.sidebar.radio("Nutritional Quality", ["Yes", "No"]) == "Yes"
    nova_quality = st.sidebar.radio("Nova Quality", ["Yes", "No"]) == "Yes"
    glisemic_quality = st.sidebar.radio("Glisemic Quality", ["Yes", "No"]) == "Yes"


