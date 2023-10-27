import pandas as pd

# creating the data

#data = [["Hazel", "Tom", "Ulysses", "Sarah", "Daniel"], [21, 31, 24, 20, 25], ["Austin", "Baton Rouge", "San Marcos", "Cedar Park", "Dripping Springs"]]
data = [["Hazel", 21, "Austin"], ["Tom", 36, "Kyle"], ["Ulysees", 26, "San Marcos"], ["Sarah", 21, "Austin"], ["Daniel", 25, "Austin"]]

# creating the dataframe

df = pd.DataFrame(data, columns = ["name", "age", "city"])

# print dataframe

# print(df)

# getting the first 3 rows from df

df_first_3 = df.head(3)

# print the first 3

print(df_first_3)

# get and print the last 2 rows

df_last_2 = df.tail(2)

print(df_last_2)

# filter for ages greater than 25

print(df[df['age'] > 25])
