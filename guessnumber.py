print('Would you like to play a game?')
answer = input("Enter yes or no: ")
if answer == "yes":
    print('wonderful!')
elif answer == "no":
    print('too bad!')
else:
    print("Please enter yes or no.")
print("I'm thinking of a number between 1 and 100.")
print("Do you think you can guess what it is?")
print("I will give you 7 guesses")
from random import randint
mynum = randint(1,100)
guesses = [0]
while True:
    guess = int(input("Enter your guess: "))
    if guess < 1 or guess > 100:
        print("Against the rules! Please stay between 1 and 100")
        continue
    break
while True:
    guess = int(input("Enter your guess: "))
    if guess == mynum:
        print(f"Great job, you guessed it in only {len(guesses)} guesses!")
    guesses.append(guess)
    if guesses[-2]:
        if abs(mynum-guess) < abs(mynum-guesses[-2]):
            print("Warmer!")
        else:
            print("Colder!")
    else:
        if abs(mynum-guess) <= 10:
            print("warm!")
        else:
            print("Cold!")
