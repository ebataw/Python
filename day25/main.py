
import pandas

# data = pandas.read_csv("weather-data.csv")
# print(data)
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# # print(data["temp"].mean())
# max = data["temp"].max()

# # print(data["condition"])
# # print(data.condition)

# print(data[data.temp == max ])

# data_dict = {
#     "students" : ["amy", "james", "angle"],
#     "score": [76, 56 , 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
data = pandas.read_csv("park.csv")
gray_squerl = len(data[data["Primary Fur Color"]== "Gray"])
red_squerl = len(data[data["Primary Fur Color"]== "Cinnamon"])
black_squerl = len(data[data["Primary Fur Color"]== "Black"])

print(gray_squerl)
print(red_squerl)
print(black_squerl)

data_dict = {
    "fur color": ["Gray", "Cinnamon", "Black"],
    "count" : [gray_squerl, red_squerl, black_squerl]
}



data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squerl_count.csv")
