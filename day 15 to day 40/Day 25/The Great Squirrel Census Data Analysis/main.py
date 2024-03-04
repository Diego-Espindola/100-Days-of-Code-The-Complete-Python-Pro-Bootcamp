import pandas as pd
df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
my_dict = {}
for row in df['Primary Fur Color']:
    if pd.notna(row):
        if row in my_dict:
            my_dict[row] += 1
        else:
            my_dict[row] = 1

count_df = pd.DataFrame(my_dict.items(), columns=["Primary Fur Color", 'Count'])
print(count_df)
