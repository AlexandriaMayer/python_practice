# I asked ChatGPT to give me exercises to practice and learn Pandas. 
# I'll update this as I complete the lessons it assigned me.

import pandas as pd
import numpy as np

# creating the data

data = [["Hazel", 21, "Austin"], ["Tom", 36, "Kyle"], ["Ulysees", 26, "San Marcos"], ["Sarah", 21, "Austin"], ["Daniel", 25, "Austin"]]

# creating the dataframe

df = pd.DataFrame(data, columns = ["name", "age", "city"])

# get and print the first 3 rows from df

df_first_3 = df.head(3)

print(df_first_3)

# get and print the last 2 rows

df_last_2 = df.tail(2)

print(df_last_2)

# filter and print for ages greater than 25

print(df[df['age'] > 25])

# sort by age, add senior field, change city name for Ulysses.

print(df.sort_values("age", ascending=False))

df["senior"] = np.where(df['age'] > 60, True, False)

df.loc[df['city'] == 'Kyle', 'city'] = 'Austin'
print(df)
