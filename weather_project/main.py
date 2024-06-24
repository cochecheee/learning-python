# weather = []
# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     # create temperatures list
#     temperatures = [int(row[1]) for row in data if row[1] != "temp"]

import pandas

data = pandas.read_csv("weather-data.csv")
# print(data["temp"])
# to_list(): convert series to list data
# print(data.to_dict())
list_data = data["temp"].to_list()
avg_temp = sum(list_data) / len(list_data)
print(avg_temp)
print(data["temp"].mean())

# particulare row
print(data[data.condition == "Sunny"])
print(data[data.temp == data.temp.max()])

# create table from dictionary
student_score = {
    "name" : ["tien","thuy","truc","nguyen"],
    "score" : [10,10,10,10]
}
data1 = pandas.DataFrame(student_score)
data1.to_csv("score-data.csv")