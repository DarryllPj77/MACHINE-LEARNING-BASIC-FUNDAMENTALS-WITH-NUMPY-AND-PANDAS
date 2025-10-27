import numpy as np

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]

#adults = ages[ages >= 18] output : [21 19 20 30 18 65 39 22 99 18 19 20 21]

adults1 = ages[(ages >= 18) | (ages < 65)]

adults2 = ages[(ages >= 18) & (ages < 65)]

adults2 = ages[(ages >= 18) & (ages < 65)]

seniors1 = ages[ages >= 65]

evens = ages[ages % 2 == 0]

odds = ages[ages % 2 != 0]

adults = np.where(ages >= 18, ages , 0)

#evens = ages[ages]
#print(teenagers)

# print(adults1)

# print(adults2)

# print(evens)

# print(odds)

print(adults)


