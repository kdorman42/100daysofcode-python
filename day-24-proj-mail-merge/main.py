#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Note - can also use file.readlines() to get names into list with \n character at the end
# and use strip() to remove the newline

PLACEHOLDER = '[name]'

with open("./Input/Names/invited_names.txt") as names_file:
    invitees_list = names_file.read().rsplit('\n')
    print(invitees_list)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_template = letter_file.read()

for invitee in invitees_list:
    new_letter = letter_template.replace(PLACEHOLDER, invitee)
    with open(f"./Output/ReadyToSend/letter_for_{invitee.lower()}.txt", mode="w") as new_file:
        new_file.write(new_letter)
