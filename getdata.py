#  #get paris weather from past week
# import pandas as pd

# import requests
# from datetime import datetime , timedelta

# today = datetime.now()
# week_ago = today - timedelta(days=7)

# #formats dates for api call(yyyy-mm-dd)
# start_date = week_ago.strftime("%Y-%m-%d")
# end_date = today.strftime("%Y-%m-%d")

# #i don't have a api key so i will not be able to run this code but this is how you can get the weather data for paris from past week
# #isnt there any opensource api for weather data? cant we use api.open-meteo.com for this?
# #yes we can use api.open-meteo.com for this. here is the code to
# url = f"https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Europe%2FBerlin"

# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     print("Weather data for Paris from the past week:")
#     print(data)

#     # can we get the data in a more readable format? like a table or a csv file?
#     # yes we can convert the data to a pandas dataframe and then save it as a csv
#     #how?


#     df = pd.DataFrame(data['daily'])
#     df.head()


# class dog:
#     def __init__(self , name , age):
#         self.name = name
#         self.age = age
#         self.breed = "labrador"

# dog1 = dog("tyson" , 9);
# print(dog1)


# from dotenv import load_dotenv
# import os

# load_dotenv()                      # 1. reads .env, loads it into the environment

# api_key = os.getenv("api_key")     # 2. fetch a value by its key name
# db_url  = os.getenv("database_url")

# print(api_key)                     # 3. use it


import sys
import os
import math
from collections import *

x = 10
y = [
    1,
    2,
    3,
    4,
]


def bad_function(a, b):
    if a == None:
        print("A is none")
    try:
        res = x / 0
    except:
        pass
    return a + b


def unused_var_func():
    unused_variable = 42
    print("Hello world")


if __name__ == "__main__":
    bad_function(1, 2)
