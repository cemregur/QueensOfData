import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)

df_ = pd.read_excel("/Users/cemregur/QueensOfData/finalProject/new_spagetti.xlsx")
df = df_.copy()
df.head()


# Calculate the glycemic index
def calculate_glycemic_index(row):
    carbohydrates = row['carbohydrates_value']
    fiber = row['fiber_value']
    sugars = row['sugars_value']
    proteins = row['proteins_value']
    fats = row['fat_value']

    glycemic_index = (carbohydrates - fiber + 0.1 * sugars + 0.15 * proteins + 0.1 * fats)
    return glycemic_index


# Calculate glycemic index column and add to DataFrame
df['glycemic_index'] = df.apply(calculate_glycemic_index, axis=1)
print(df)
df.head()

# Foods according to their glycemic index in the literature
# classified as low (1-55), moderate (56-69), and high (>70) GI.

# Create a categorical column
df['GI_category'] = pd.cut(df['glycemic_index'], bins=[0, 55, 69, float('inf')],
                           labels=['low_gi', 'medium_gi', 'high_gi'], right=False)

print(df)

# user_preferences

# Create Streamlit App

# Step 1: Category Selection

import streamlit as st

st.set_page_config(
    page_title="Safe Food For Everyone",
    page_icon="path_of_your_favicon",
    layout="wide",
    initial_sidebar_state="auto",
)
st.subheader("Step 1: Select Product Category")

selected_category = st.selectbox("Select Product Category", df["categories"].unique())

# Define selected_allergens outside of the "Preferences" section
selected_allergens = []
# Define nutritional_quality, nova_quality, and glisemic_quality outside of the "Preferences" section
nutritional_quality = False
nova_quality = False
glisemic_quality = False
# Step 2: Preferences
# create "Preferences" button
show_preferences = st.button("Edit Preferences")
# Show preferences page when clicking "Preferences" button
if show_preferences:
    st.title("Preferences")

    # Get Nutritional Quality, Nova Quality ve Glisemic Quality choices with default values
    st.subheader("Nutritional Quality")
    nutritional_quality = st.radio("Nutritional Quality", ["Yes", "No"], index=1) == "Yes"

    st.subheader("Nova Quality")
    nova_quality = st.radio("Nova Quality", ["Yes", "No"], index=1) == "Yes"

    st.subheader("Glisemic Quality")
    glisemic_quality = st.radio("Glisemic Quality", ["Yes", "No"], index=1) == "Yes"

    # Get Allergen choices with a default value of 0 (None selected)
    st.subheader("Allergen")
    selected_allergens = st.multiselect("Allergen", ["Milk", "Gluten", "Egg", "Peanut", "Soybeans", "Nut"], default=[])
# create query based on allergens
preference_query = True
if selected_allergens and selected_allergens[0] != 0:
    allergen_query = df["allergens"].str.contains(selected_allergens[0], case=False, na=False)
    for allergen in selected_allergens[1:]:
        allergen_query |= df["allergens"].str.contains(allergen, case=False, na=False)
else:
    allergen_query = False

# Create the main query based on preferences (for example: nutritional quality, nova quality, glycemic quality)
preference_query = (
        (df["off:nutriscore_grade"] == nutritional_quality) &
        (df["off:nova_groups"] == nova_quality) &
        (df["GI_category"] == glisemic_quality)
)

# Create final query based on allergen and preferences
final_query = preference_query & allergen_query

# Print results to screen
st.subheader(f"{selected_category} category results")

for index, row in df[final_query].iterrows():
    st.write(f"**Product Name:** {row['product_name_fr_it']}")
    st.write(f"**Nutriscore Grade:** {row['off:nutriscore_grade']}")
    st.write(f"**Nova Groups:** {row['off:nova_groups']}")
    st.write(f"**GI Category:** {row['GI_category']}")
    st.write(f"**Brand:** {row['brands']}")
    st.write(f"**Ingredients (EN):** {row['ingredients_text_en']}")

    for allergen in selected_allergens:
        allergen_column = f"Allergen_{allergen}"
        allergen_status = "Contains" if row[allergen_column] == "yes" else "Not Contains"
        st.write(f"**{allergen} Allergen:** {allergen_status}")

    st.write("---")
