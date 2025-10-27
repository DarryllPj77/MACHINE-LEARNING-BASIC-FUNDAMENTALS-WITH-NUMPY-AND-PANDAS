import pandas as pd

df = pd.read_csv("Data In CSV\sales_data_150.csv")

#SELECTION BY COLUMN
# Transaction_ID,
# Product_Category,
# Quantity,
# Price_Per_Unit,
# Sale_Amount


print(df["Product_Category"].to_string())