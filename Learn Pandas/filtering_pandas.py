import pandas as pd

df = pd.read_csv("Data In CSV\pokemon_data_150.csv")

#Filtering = Keeping the rows that match a condition

tall_pokemon = df[df["Height"] >= 2] 

havy_pokemon = df[df["Weight"] > 100]

legendary_pokemon = df[df["Legendary"] == 1]

water_pokemon1 = df[df["Type1"] == "Water"]

water_pokemon2 = df[(df["Type1"] == "Water")| 
                    (df["Type2"] == "Water")]

ff_pokemon = df[(df["Type1"] == "Fire") &
                (df["Type2"] == "Flying")]

#print(tall_pokemon)

#print(havy_pokemon)

#print(legendary_pokemon)

#print(water_pokemon2)

print(ff_pokemon)

