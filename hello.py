# class person:
#     def person_details(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city

#         return f"Name: {self.name}, Age: {self.age}, City: {self.city}"

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# city = input("Enter your city: ")

# p = person()
# print(p.person_details(name, age, city))

# first_name = "sagar"
# last_name = "sharma"

# full_name = first_name + " " + last_name
# print(full_name)
# namelen = len(full_name)
# print(namelen)


#how to make arrays in python
# my_list = [1,2,3,5,6,2]
# print(my_list[3])
# my_list.insert(1 , 122)
# print(my_list)

#take an array as input and return the second largest elemnent of array/list in python.
# def second_largest(arr):
#     unique_arr = list(set(arr))
#     unique_arr.sort(reverse = True)
#     return unique_arr[1];
# #how to input an array in p'ython
# arr = list(map(int , input("Enter the elements of the array separated by space: ").split()))
# result = second_largest(arr)
# print(arr)
# print("The second largest element in the array is:", result)    

# # how to initialize maps in python
# map = {"name": "sagar", "age": 22, "city": "delhi"}
# #adding new key-value pair in map
# map["country"] = "India"
# print(map)

# #strings in py
# str = "new string"
# print(str[0:3]) #new
# print(str[4:10]) #string

# # str[0 : 3] = "oldieee"  # This will cause an error because strings are immutable in Python
# str = "oldieee" + str[3:]  # This is the correct way to modify a string
# print(str)  # Output: oldiee string

# def greet(last_name , first_name = "sagar"):
#     print(f"hello, {first_name} {last_name}")

# greet("sharma")


# #lets do linear search in python
# def linear_search(arr , target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# arr = [1,4,5,2,9,5]
# target = 5
# result = linear_search(arr, target)
# print(f"Element {target} found at index: {result}")


# import random
# def random_number():
#     return random.randint(1, 100)
# number = random_number()
# print (number)




#first api call with pythion
import requests 
url = "https://pokeapi.co/api/v2/pokemon/ditto"
response = requests.get(url)
if response.status_code == 200:
    print("API call successful!")
    print(response.json())
else:
    print("API call failed with status code:", response.status_code)