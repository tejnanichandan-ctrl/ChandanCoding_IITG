import pandas as pd

df = pd.read_csv("sales_data_india.csv")

print(df) # Display the entire DataFrame
print(df.head()) # Display the first 5 rows
print(df["TotalPrice"].sum()) # Display the sum of TotalPrice
print(df["Product"].value_counts()) # Display the count of each product
print(df.info()) # Display information about the DataFrame
print(df.describe()) # Display summary statistics of the DataFrame
print(df.groupby("Category")["TotalPrice"].sum()) # Display total sales by category
print(df.loc[df["PricePerUnit"].idxmax()]) # Display the row with the highest PricePerUnit
