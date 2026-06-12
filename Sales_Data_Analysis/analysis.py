import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

df["Total_Sales"] = df["Quantity"] * df["Price"]

total_sales = df["Total_Sales"].sum()
print("Total Sales:", total_sales)

product_sales = df.groupby("Product")["Total_Sales"].sum()
print(product_sales)

top_product = product_sales.idxmax()
print("Best Selling Product:", top_product)

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.savefig("sales_chart.png")
plt.show()