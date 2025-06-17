import random
import hangman_words
import hangman_art
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
display = ["_"]*len(chosen_word)
while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.

    guess = input("Guess a letter: ").lower()


    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    for letter in chosen_word:
        if guess == letter:

            list1 = []



            for index, item in enumerate(chosen_word):
                if chosen_word[index] == guess:
                    list1.append(index)
            for i in list1:
                display[i] = guess
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
    correct_letters.append(guess)
    print("".join(display))


    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess},that's not in the word.You lose a life")

    if lives == 0:
        game_over = True

       
        print(f"It was {chosen_word}!")
        print(f"***********************YOU LOSE**********************")
    print(hangman_art.stages[lives])
    print(f"****************************<???>{lives} LIVES LEFT ****************************")
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

   


