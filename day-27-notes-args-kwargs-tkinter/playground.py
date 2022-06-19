# # Advanced Python Arguments
# # args are required, kwargs are not
# # use a default value to implement
# def my_function(a=1, b=2, c=3):
#     do this with a
#     then do this with b
#     then do this with c
# # in the above, can change the keyword arguments but will be default if not changed
#
#
# # Unlimited arguments
# def add(*args):  # asterix tells python any number of arguments can be added
#     for n in args:
#         print n


# def add(*args):
#     total = 0
#     for a in args:
#         total += a
#     return total
#
#
# sum = add(1, 2, 5, 7)
# sum2 = add(56, 2345, 76, 2, 5636, 5, 3)
# print(sum, sum2)
#
#
# def calculate(n, **kwargs):
#     # print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#     # print(kwargs["add"])
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=3, multiply=5)


# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         # self.model = kw["model"]  # returns an error if missing
#         self.model = kw.get("model")  # returns "None" if missing
#         self.color = kw.get("color")
#
#
# my_car = Car(make="Nissan", model="GTR")
# print(my_car.model)
# print(my_car.make)
