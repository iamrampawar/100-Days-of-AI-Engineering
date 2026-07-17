secret_number = 7

while True:
    guess = int(input("Enter a number(1,10)"))
    if guess == secret_number:
        print("Congratulations! you guess the correct number")
        break
    else:
        print("Wrong guess , try again")