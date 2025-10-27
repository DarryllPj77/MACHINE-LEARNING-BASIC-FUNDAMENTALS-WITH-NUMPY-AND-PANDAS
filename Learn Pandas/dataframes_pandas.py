import pandas as pd

# data = {
#     "Name" : ["Employee1", "Employee2", "Employee3"],
#     "Age" : ["30","40","50"]
# }

# df = pd.DataFrame(data)

#print(df)
# output
# Name Age
# 0  Employee1  30
# 1  Employee2  40
# 2  Employee3  50

data = {
    "Name" : ["Person 1", "Person 2", "Person 3"],
    "Age" : ["30","40","50"]
}

df = pd.DataFrame(data, index = ["Employee 1","Employee 2","Employee 3"])

#print(df)
# output
#                 Name Age
# Employee 1  Person 1  30
# Employee 2  Person 2  40
# Employee 3  Person 3  50

#print(df.loc["Employee 1"])
# output
# Name    Person 1
# Age           30
# Name: Employee 1, dtype: object

#print(df.loc["Employee 2"])
# output
# Age           40
# Name: Employee 2, dtype: object

#print(df.iloc[1])
# output
# Name    Person 2
# Age           40
# Name: Employee 2, dtype: object

#add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

# print(df)

#Add a new row
new_row = pd.DataFrame([{"Name": "Person 4", "Age": 28, "Job": "Engineer"},
                        {"Name": "Person 5", "Age": 29, "Job": "Manager"},
                        {"Name": "Person 6", "Age": 31, "Job": "Data Science"},
                        {"Name": "Person 7", "Age": 32, "Job": "Project Management"}],
                       index = ["Employee 4",
                                "Employee 5",
                                "Employee 6",
                                "Employee 7"])
df = pd.concat([df, new_row])

print(df)
# output
#                 Name Age       Job
# Employee 1  Person 1  30      Cook
# Employee 2  Person 2  40       N/A
# Employee 3  Person 3  50   Cashier
# 0           Person 4  28  Engineer