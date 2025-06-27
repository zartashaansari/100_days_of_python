#start of program
import random
import art
attempts=0
print(art.logo)
print("Welcome to the number guessing game\n")
difficulty_level=input("Choose difficulty level : Easy or Hard\n ").lower()
num_to_guess=random.randint(1,100)

if difficulty_level=='hard':
    attempts=5
    print("you have got 5 attempts 😊!")
else:
    attempts=10
    print("you have got 10 attempts 😊!")

for i in range(attempts):
    guess=int(input("Guess a number between 1 and 100\n"))

    if guess==num_to_guess:
        print("OLA YOU WIN CHAMP 🥳!!!")
        break
    elif  guess< num_to_guess:
        print("TOO LOW ⬇️!")
        attempts -= 1
        print(f"You have {attempts} attempts left!️")
    elif guess>num_to_guess:
        print("TOO HIGH ⬆️!")
        attempts -= 1
        print(f"You have {attempts} attempts left!")
else:
    print("YOU LOSE 😔")
