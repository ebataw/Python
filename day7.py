
import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

x=random.randint(0,3-1)
chosen_word=word_list[x]
print(chosen_word)

user_solution = []
for t in range(0,len(chosen_word)):
    user_solution.append("_")

print(" ".join(user_solution))

guess=input("guess a letter: ").lower()
if guess in chosen_word:
    letter_index=chosen_word.index(guess)
    print(letter_index)
    user_solution[letter_index] = guess
    print(" ".join(user_solution))

