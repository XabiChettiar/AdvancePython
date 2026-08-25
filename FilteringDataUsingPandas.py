import pandas as pd

df = pd.DataFrame({
    "Product Name": [" iPhone 14 ", "Samsung Galaxy", " OnePlus 11", "Pixel 7 ", None] * 200,
    "price": ["499", "799", "1199", "899", None] * 200,
    "category": ["Mobile", " mobile ", "ELECTRONICS", "Electronics ", None] * 200,
    "rating": [5, 4, None, 3, 2] * 200,
    "reviews": [1200, 3400, 560, 780, 150] * 200,
    "in_stock": ["Yes", "No", "yes ", " no", None] * 200,
    "launch_year": ["2023", "2022", "2021", "2020", None] * 200
})



# print(df)

# print(df[['Product Name','price']])

# print(df[df['in_stock']=='Yes'])

# print(df[(df['reviews']>500) & (df['in_stock']=='Yes')])

# print(df[df['rating']==5])

# print(df.isna().sum())

# print(df.dropna())

# df['rating']=df["rating"].fillna(df["rating"].mean())

# df['rating']=df["rating"].fillna(1)

# print(df[df["rating"]==1])

# df=df.rename(columns={"price":"Price"})

# df['launch_year']=df["launch_year"].astype(float)

# print(df.dtypes)

# print(df[df["launch_year"]<=2020])


df['in_stock']=df["in_stock"].str.lower().str.strip()

print(df[df["in_stock"]=='yes'])