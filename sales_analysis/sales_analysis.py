import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print("Dataset preview")
print(df.head())

total_sales = df["Amount"].sum()
print("\n Total sales : ", total_sales)

category_sales = df.groupby("Category")["Amount"].sum()
print("\n Sales by Category : ", category_sales)

city_sales = df.groupby("City")["Amount"].sum()
print("Sales by City : ", city_sales)

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()
