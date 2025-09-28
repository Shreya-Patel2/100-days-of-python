import pandas as pd

nato_phonetic_alphabet_csv = pd.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alphabet = pd.DataFrame(nato_phonetic_alphabet_csv)
#print(nato_phonetic_alphabet)

data = {row.letter:row.code for (index, row) in nato_phonetic_alphabet.iterrows()}
#print(data)

word = input("Enter a word").upper()
#print(word)

letter_list = [letter for letter in word]
#print(letter_list)

phonetic_word = [data[letter] for letter in letter_list]
print(phonetic_word)

