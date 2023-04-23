import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')

dic_df = {row.letter: row.code for (index, row) in df.iterrows()}

user_input = input("Type your words for Nato Phonetic conversion \n")

user_input = [letters.upper() for letters in user_input]

output = [dic_df[letters] for letters in user_input]

print(output)
