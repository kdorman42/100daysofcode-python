
# # Using previous file text handling isn't ideal. See example:
# with open('weather_data.csv') as file:
#     data = file.read().rsplit(sep='\n')
# print(data)


# # Instead use python's built-in CSV functionality
# # This puts  rows into lists
# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
# print(temperatures)


# Pandas is way better for CSVs!
# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# print(data["temp"])
# print(type(data))  # data is a DataFrame
# print(type(data["temp"]))  # data["temp"] is a Series

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# Calculating the mean - pandas has built in calculations
# average_temp = round(sum(data["temp"]) / len(data["temp"]))
# average_temp = round(data["temp"].mean())  # uses built-in pandas calc methods
# max_temp = data["temp"].max()
# print(max_temp)
# print(data.temp)  # can also be referred to like this instead of data["temp"]

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])  # print the day's record with the max temp

# monday = data[data.day == "Monday"]
# print(monday.temp * 9/5 + 32)  # convert monday's temp to fahrenheit

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data_df = pandas.DataFrame(data_dict)
# data_df.to_csv("new_data.csv")


# Challenge: Output a CSV of count by fur color
import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
summary = data[["Primary Fur Color", "Unique Squirrel ID"]].groupby(["Primary Fur Color"]).count().reset_index()
summary = summary.rename(columns={"Unique Squirrel ID": "Count", "Primary Fur Color": "Fur Color"})
print(summary)
summary.to_csv('Squirrel Count By Color')
