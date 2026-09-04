import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data
sales = pd.read_csv("sales_data.csv")

# Convert Date to datetime
sales["Date"] = pd.to_datetime(sales["Date"])

print("First 5 rows:")
print(sales.head())

print("\nDataset shape:", sales.shape)
print("\nDataset information:")
sales.info()

print("\nMissing values:")
print(sales.isnull().sum())

# Overall sales summary
print("\nTotal sales: ₹", sales["Total_Sales"].sum())
print("Total quantity sold:", sales["Quantity"].sum())
print("Average order value: ₹", round(sales["Total_Sales"].mean(), 2))

# Sales by category
category_sales = sales.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)
print("\nSales by category:")
print(category_sales)

# Sales by region
region_sales = sales.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
print("\nSales by region:")
print(region_sales)

# Product performance
product_sales = sales.groupby("Product").agg(
    Total_Sales=("Total_Sales", "sum"),
    Quantity_Sold=("Quantity", "sum")
).sort_values("Total_Sales", ascending=False)
print("\nProduct performance:")
print(product_sales)

# Monthly sales
monthly_sales = sales.groupby(sales["Date"].dt.to_period("M"))["Total_Sales"].sum()
print("\nMonthly sales:")
print(monthly_sales)

# Top order
best_order = sales.loc[sales["Total_Sales"].idxmax()]
print("\nHighest-value order:")
print(best_order)

# Chart 1: Sales by category
category_sales.plot(kind="bar", title="Total Sales by Category", xlabel="Category", ylabel="Sales (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Chart 2: Sales by region
region_sales.plot(kind="bar", title="Total Sales by Region", xlabel="Region", ylabel="Sales (₹)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Chart 3: Monthly sales trend
monthly_sales.astype(float).plot(kind="line", marker="o", title="Monthly Sales Trend", xlabel="Month", ylabel="Sales (₹)")
plt.tight_layout()
plt.show()

# Key findings
print("\nKEY FINDINGS")
print(f"1. Total revenue generated: ₹{sales['Total_Sales'].sum():,.0f}")
print(f"2. Best-performing category: {category_sales.index[0]}")
print(f"3. Best-performing region: {region_sales.index[0]}")
print(f"4. Best-selling product by revenue: {product_sales.index[0]}")
print(f"5. Highest-value order: ₹{sales['Total_Sales'].max():,.0f}")
