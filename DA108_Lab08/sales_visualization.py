import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("DA108_Lab08/sales_data_india.csv")

# Group by category and sum the total price
# This will give us the total sales for each category
sales_category = df.groupby("Category")["TotalPrice"].sum()

sales_category.plot(kind="bar")

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show() # Display the bar chart

daily_sales = df.groupby("Date")["TotalPrice"].sum()

daily_sales.plot()

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")

plt.show() # Display the line chart

city_sales = df.groupby("City")["TotalPrice"].sum()

city_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Sales Distribution by City")

plt.show() # Display the pie chart 