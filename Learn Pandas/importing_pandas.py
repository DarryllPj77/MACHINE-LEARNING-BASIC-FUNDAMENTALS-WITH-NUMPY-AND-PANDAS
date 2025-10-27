import pandas as pd
''''''
# #Importing CSV dataset with 150 rows of Sales Transactions

# df = pd.read_csv("Data In CSV\sales_data_150.csv")

# # Convert all cells to string and center them with a fixed width (e.g., 15)
# df = df.astype(str).applymap(lambda x: x.center(15))


# print(df.to_string(index=False))


# #print(df.to_string(index = False)) #Remove indexn when printing

''''''
# #Importing JSON dataset with 150 rows of Sales Transactions

df = pd.read_json("Data In CSV\sales_data_150.json")

print(df.to_string())