import pandas as pd


df = pd.read_csv(
    "C:/Users/Mohammadi/Desktop/Coursera/personal-project/course-1/amazon_laptop_prices_v01.csv"
)
# print(len(df["brand"].unique()))
df["brand"] = df["brand"].str.lower()
print(df["brand"].value_counts())
