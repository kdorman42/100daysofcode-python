# Reading from text files

# # file = open('my_text.txt')  # using "with" below, no need for open/close commands.
# with open('my_text.txt') as file:
#     contents = file.read()
#     print(contents)
#     # file.close()

# with open('my_text.txt') as file:  # set to read only by default, won't work
#     file.write("New text.")


# Overwrites existing text
# with open('my_text.txt', mode='w') as file:
#     file.write("New text.")
#
# with open('my_text.txt') as file:
#     contents = file.read()
#     print(contents)


# # Appends text to existing text
# with open('my_text.txt', mode='a') as file:
#     file.write("\nNew text.")
#
# with open('my_text.txt') as file:
#     contents = file.read()
#     print(contents)


# If file does not exist, new file is created
# with open('new_file.txt', mode='w') as file:
#     file.write("New text.")


# Understanding Relative and Absolute File Paths
# Absolute file paths always start at the root ("/Work/Project/talk.ppt")
# Relative file paths are relative from the working directory ("./talk.ppt")
# Getting a file from folder relative to working directory, e.g. Work folder: ("../talk.ppt")
# No need for "./" for relative path at the same level.

# Moved file to desktop...
# Use forward instead of backslashes in full file path
# with open('/Users/kdorman/Desktop/my_text.txt') as file:  # Absolute path
# with open("../../Desktop/my_text.txt") as file:  # relative path
#     contents = file.read()
#     print(contents)