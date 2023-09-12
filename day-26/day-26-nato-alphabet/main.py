import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

alphabet_df = pandas.read_csv('./nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

user_input = input("Enter a word: ").upper()
output = [alphabet_dict[letter] for letter in user_input]
print(output)
