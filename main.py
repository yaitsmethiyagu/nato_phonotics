import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')

dictionary_df = {row.letter: row.code for (index, row) in df.iterrows()}


def get_input():
    user_input = input("Type your words for Nato Phonetic conversion \n").upper()
    try:
        output = [dictionary_df[letters] for letters in user_input]
    except KeyError:
        print("Sorry only Alphabetic")
        get_input()
    else:
        print(output)

while 1:
    get_input()
