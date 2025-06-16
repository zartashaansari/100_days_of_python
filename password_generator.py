letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

length_of_pwd=nr_letters+nr_numbers+nr_symbols
import random
final=[]
count_of_letters=0
count_of_numbers=0
count_of_symbols=0
while length_of_pwd!=0:
    trick=[1,2,3]
    goto=random.choice(trick)
    if goto==1:
        if count_of_letters !=  nr_letters:

            final.append(random.choice(letters))
            count_of_letters+=1
            length_of_pwd-=1
    elif goto==2:
        if count_of_symbols!= nr_symbols:

            final.append(random.choice(symbols))
            count_of_symbols+=1
            length_of_pwd -= 1

    elif goto==3:
        if count_of_numbers != nr_numbers:

            final.append(random.choice(numbers))
            count_of_numbers+=1
            length_of_pwd -= 1
pwd="".join(final)
print(pwd)
#alternative approach
password_chars = (
    random.choices(letters, k=nr_letters) +
    random.choices(symbols, k=nr_symbols) +
    random.choices(numbers, k=nr_numbers)
)

random.shuffle(password_chars)
password = ''.join(password_chars)
print(password)