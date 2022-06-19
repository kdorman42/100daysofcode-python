# Day 30: Errors, Exceptions, and JSON

# # traceback error:
# with open("some_file.txt") as file:
#     file.read()

# # key error:
# a_dictionary = {"key": "value"}
# value = a_dictionary["nonexistent_key"]

# # Index Error:
# fruit_list = ["fruit1", "fruit2"]
# fruit = fruit_list[20]

# type error:
# text = "abc"
# print(text + 5)

# try catch except finally
# try: something that might cause an exception
# except: to this if there was an exception - note: ignores ALL errors - need to be more specific
# else: do this if there were no exceptions
# finally: do this no matter what happens

# # traceback error example
# # with open("a_file.txt") as file:
# #     file.read()
# try:
#     file = open("some_file.txt")
#     print(a_dictionary["wuwtyt"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print("File was closed.")
#     raise KeyError ("This is an error that I made up.")



# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")
#
# bmi = weight / height ** 2
# print(bmi)


#------------------------------------

# Write, read, and update JSON data in the Password Manager
# json.load, json.dump, json.update
# json.load() returns type dict
