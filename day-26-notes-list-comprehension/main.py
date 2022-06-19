
# # List Comprehension

# shortcut for making new lists from existing lists

# format - replace keywords new_item, item, and list:  new_list = [new_item for item in list]

# numbers = [1, 2, 3]
# # new_list = []
# # for n in numbers:
# #     add_1 = n + 1
# #     new_list.append(add_1)
#
# # replaces the above
# new_list = [n + 1 for n in numbers]
# print(new_list)

# --------------------

# Python Sequences: list, range, string, tuple
# list comprehension works on all of them, returns a list

# name = "Angela"
# letters_list = [letter for letter in name]  # turns string into individual letters in a list
# print(letters_list)

# # Practice with a range sequence
# r = range(1, 5)
# doubled_range = [n * 2 for n in r]
# print(doubled_range)

# ----------------------

# # Conditional List Comprehension
# format:  new_list = [new_item for item in list if test]

# Example
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)

# Practice
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# ----------------------

# # Dictionary Comprehension

# format:  new_dict = {new_key: new_value for item in list if test}
# another format: new_dict = {new_key: new_value for (key, value) in dict.items() if test}

# import random
# students_scores = {name:random.randint(1, 100) for name in names}
# passed_students = {name:score for (name, score) in students_scores.items() if score > 60}

# ----------------------

# # Iterating over a Pandas DataFrame

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

# import pandas as pd
#
# student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
# index is row number in table

# for (index, row) in student_data_frame.iterrows():
#     print(row)
#     print(row.score)

for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)


# format for pandas? {new_key:new_value for (index, row) in df.iterrows()}


