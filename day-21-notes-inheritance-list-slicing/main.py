# Class Inheritance

# Chef example:
#------------------
# Chef
#
# bake()
# stir()
# measure()
#
# Pastry Chef
# bake()
# stir()
# measure()
# crack_eggs()
# sift_flour()


# class Fish(Animal) example
#------------------
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, exhale.")
#
#
# class Fish(Animal):
#
#     def __init__(self):
#         super().__init__()  # Initialize everything Animal class can do
#
#     def breathe(self):
#         super().breathe()  # extends from the super class
#         print("doing this underwater.")
#
#     def swim(self):
#         print("moving in water.")
#
# nemo = Fish()
# nemo.swim()



# Slicing
#--------------------

piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
piano_tuple = ['do', 're', 'mi', 'fa', 'so', 'la', 'ti', 'do']

print(piano_keys[2:5])
print(piano_keys[2:])
print(piano_keys[:5])
print(piano_keys[2:5:2]) # last number is step parameter (in this example, skip one
print(piano_keys[::-1]) # list but backwards bc of negative one

# the above also works with tuples
print(piano_tuple[2:5])