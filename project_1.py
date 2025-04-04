
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
df = files.upload()

df = pd.read_csv("sales_data.csv")


product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending = False)
print("*******most_sales*******")
print(product_sales)
print("*******city_sales*******")
city_sales = df.groupby("City")["Total_Sales"].sum().sort_values(ascending = False)
print(city_sales)
print("*******category_compartion*******")
category_sales = df.groupby("Category")["Total_Sales"].sum()
print(category_sales)

plt.figure(figsize=(8, 6))
sns.barplot(x=product_sales.index, y=product_sales.values, palette="Blues_d")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

plt.figure(figsize=(8,6))
sns.barplot(x=city_sales.index, y=city_sales.values, palette="Greens_d")
plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.show()

