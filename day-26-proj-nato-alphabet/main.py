
import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')

# Keyword Method with iterrows()
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 1. Create a dictionary in this format:  {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():

    user_input = input("Enter a word:  ").upper()

    try:
        new_list = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(new_list)


generate_phonetic()
