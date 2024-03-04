import pandas as pd

data = pd.read_csv("weather_data.csv")

#print(data['temp'])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# data_list = data.temp
# average = data_list.max()
# print(f"Average= {round(average, 2)}")

monday = data[data.day == "Monday"]
temp = (monday.temp * 9/5) + 32
print(temp)
