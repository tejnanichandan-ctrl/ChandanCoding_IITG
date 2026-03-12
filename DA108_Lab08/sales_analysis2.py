import pandas as pd

class SalesDataProcessor:

    def __init__(self): # Initialize the SalesDataProcessor class
        self.df = None

    def load_data(self, file_path): # Load data from a CSV file
        self.df = pd.read_csv(file_path)

    def clean_data(self): # Clean the data by removing null values
        self.df = self.df.dropna()

    def get_total_sales(self): # Get the total sales amount
        return self.df["TotalPrice"].sum()

    def get_unique_products(self): # Get unique products sold
        return self.df["Product"].unique()

    def get_sales_by_category(self): # Get sales by category
        return self.df.groupby("Category")["TotalPrice"].sum()

    def get_top_selling_product(self): # Get the top-selling product
        sales = self.df.groupby("Product")["Quantity"].sum()
        return sales.idxmax()
    
class CustomerSalesProcessor(SalesDataProcessor):

    def get_total_sales_by_customer(self, customer_id):
        customer_data = self.df[self.df["CustomerID"] == customer_id]
        return customer_data["TotalPrice"].sum()

    def get_frequent_customers(self, n):
        return self.df["CustomerID"].value_counts().head(n)

    def get_sales_by_city(self):
        return self.df.groupby("City")["TotalPrice"].sum()    
    
processor = CustomerSalesProcessor()

processor.load_data("DA108_Lab08/sales_data_india.csv")

print("Total Sales:", processor.get_total_sales())

print("Unique Products:")
print(processor.get_unique_products())

print("Sales by Category:")
print(processor.get_sales_by_category())

print("Top Selling Product:", processor.get_top_selling_product())

print("Sales by City:")
print(processor.get_sales_by_city())

print("Frequent Customers:")
print(processor.get_frequent_customers(3))    

class CustomerSalesProcessor(SalesDataProcessor):

    def get_total_sales_by_customer(self, customer_id):
        customer_data = self.df[self.df["CustomerID"] == customer_id]
        return customer_data["TotalPrice"].sum()

    def get_frequent_customers(self, n):
        return self.df["CustomerID"].value_counts().head(n)

    def get_sales_by_city(self):
        return self.df.groupby("City")["TotalPrice"].sum()
    
    processor = CustomerSalesProcessor()

processor.load_data("DA108_Lab08/sales_data_india.csv")

print("Total Sales:", processor.get_total_sales())

print("Unique Products:")
print(processor.get_unique_products())

print("Sales by Category:")
print(processor.get_sales_by_category())

print("Top Selling Product:", processor.get_top_selling_product())

print("Sales by City:")
print(processor.get_sales_by_city())

print("Frequent Customers:")
print(processor.get_frequent_customers(3))