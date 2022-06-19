# # Creating Classes in Python
#
# # Class names are PascalCase
# # They aren't camelCase (not much camelCase)
# # snake_case is used for pretty much everything else
#
#
# class User:
# #    pass # gets rid of errors related to empty class or function
#
#     def __init__(self, user_id, username): # allows to set requirements and defaults for attributes
#         # self is object itself (in this case User)
#         # multiple things def __init__(self, seats) ... seats is another attribute
#         # print("new user being created...")
#         self.id = user_id
#         self.username = username
#         self.followers = 0  # 0 is the default value
#         self.following = 0
#
#     def follow(self, user): # a method is just a function associated with a class
#         user.followers += 1
#         self.following += 1
#
#
# # Creating each object on its own is error prone
# user_1 = User("001", "angela")
# # user_1.id = "001"
# # user_1.username = "angela"
# # print(user_1.username)
#
# # user_2 = User()  # causes an error if required attributes are not included
# user_2 = User("002", "jack")
# # user_2.id = "002"
# # user_2.username = "jack"
# # print(user_2.username)
#
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)
