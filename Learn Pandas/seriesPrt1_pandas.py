import pandas as pd

#data = [100, 102, 103]
# output
# 0    100
# 1    102
# 2    103
# dtype: int64

#data = [100.2, 102.09, 103.66]
# output
# 0    100.20
# 1    102.09
# 2    103.66
# dtype: float64

#data = ["A", "B", "C"]
# output 
# 0    A
# 1    B
# 2    C
# dtype: object

#data = [True, False, True]
# output
# 0     True
# 1    False
# 2     True
# dtype: bool

data = [100, 102, 103, 200, 202]

series = pd.Series(data, index = ["a", "b", "c", "d", "e"])

series.loc["c"] = 200

print(series)

print(series.loc["c"]) #200
print(series.iloc[0]) #100 integer-key

print(series[series >= 200]) #printing grater than 200
print(series[series < 200]) #printing less than 200