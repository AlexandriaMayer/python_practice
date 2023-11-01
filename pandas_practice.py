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

df.loc[df['city'] == 'Kyle', 'city'] = 'Austin'
print(df)

# Amending the dataframe with rows missing age or city values.

df10272023 = [{"name": "Claire", "age": np.nan, "city": "Austin"},
              {"name": "John", "age": 21, "city": np.nan},
              {"name": "Steve", "age": 34, "city": np.nan},
              {"name": "Morgan", "age": np.nan, "city": np.nan},
              {"name": "Tyler", "age": np.nan,"city": "Tyler"},
              {"name": "Ashley", "age": 28, "city": "Austin"}]

df = df._append(df10272023, ignore_index=True)

# We are dropping the rows where the city field is null
df = df.dropna(subset=['city'])
# Had the senior check at line 36, realized it needs to be run after all amends have been made.

df["senior"] = np.where(df['age'] > 60, True, False)

print(df)

# group data by city, get average age in each city
# group data by city, get average age in each city

gr = df.groupby('city').mean('age')
names = df.groupby(['city'])['name'].count()

print(gr)
print(names)
