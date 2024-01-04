import random
import pandas as pd
from IPython.display import display

# accessing words from the file
with open("words.txt", "r") as words_file:
    words = words_file.read().split()

five_letter_words = []

while len(five_letter_words) < 300:
    word = random.choice(words)
    if len(word) == 5 and word not in five_letter_words:
        five_letter_words.append(word)

# selecting the word
w = random.choice(five_letter_words)
word = list(w.upper())

# print statements
print("----------------------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------------------|  WORDLE  |--------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------------")
print("\nYou have to guess a 5 letter word. Let's see how good you are with words!!")
print("You have 6 chances to guess the word.\n")
print("The word for you is  _ _ _ _ _")
print("""You have to enter any 5-letter word.
1. Letter in Uppercase means: Right position of letter
2. Letter in Lowercase means: Wrong position of letter
3. Letter replaced by underscore: Letter is not present in the word""")
print("\n")
print("----------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------|  LET US BEGIN  |-----------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------------")
print("\n")

# Variables we need
list_guess = []
guesses = 6
i = 1
flag = 0
j = 1
index_list = ["Guess " + str(j)]

# loop for 6 guesses
while guesses > 0:
    guess = input("Enter your guess: ")

    # checking length of entered word
    if len(guess) != 5:
        print("Length of the word is not matching! Please Retry")
        guesses += 1
        continue

    # comparing the words
    guesslist = list(guess.upper())
    printguess = ""
    for index, letter in enumerate(guesslist):
        if letter == word[index]:
            printguess += letter
        elif letter in word:
            printguess += letter.lower()
        else:
            printguess += "_"

    # entering the data into a Dataframe
    printguess = list(printguess)
    list_guess.append(printguess)
    df = pd.DataFrame(list_guess, index = index_list, columns = ["L1","L2","L3","L4","L5"])
    display(df)
    print("\n")

    if guess.upper() == w.upper():
        flag = 1
        break

    #incrementing the values
    i += 1
    j += 1
    index_list.append("Guess " + str(j))
    guesses -= 1

# printing the final statements
if flag == 1:
    print("You have guessed the word.")
    print("Congratulations!")
else:
    print("You were not able to guess the word. The word was: ", w.upper())

print("\n")
print("----------------------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------|  THANK YOU FOR PLAYING  |--------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------------------")