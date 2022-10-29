#Guess the number within 10 guesses. Print no of guesses left, print Game Over if all guesses exhausted
#You also have to give hints to user, if the lucky number is greater or smaller than the number entered
#Print Congrats, if guessed correctly and also print how many guesses the user took to guess it correctly

import random
print("Welcome to the guessing game\nYou have to guess the lucky number within 10 attempts")
print("For starters, I'll give you a small hint, the number is between 1 to 100")
num = random.randint(1,100)

i = 1
while i<=10:
    inp = int(input("Guess the number:\n"))
    if inp < num:
        print("The number you've guessed is smaller than the lucky number\nTotal attempts left: ",10-i)
    elif inp > num:
        print("The number you've guessed is greater than the lucky number\nTotal attempts left: ",10-i)
    else:
        print("Congratulations you've guessed the lucky number correctly in",i,"attempts")
        break
    i = i + 1

if i > 10:
    print("You've exhausted all your guesses.\nGAME OVER!!")
    print("Thank you for playing this game!!")