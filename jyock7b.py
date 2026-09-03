# CTC389-151
# Jeff Yock
# Lab 7
# Part 2

num = 7

def game ():
    print ("I have selected a number between 1 and 10 ")
    guess = int(input("Guess my number! "))
    while guess!= num:
        if guess < num - 2:
            print("Sorry, your guess was too low. My number was", num)
            break
        elif guess > num + 2:
            print("Sorry, your guess was too high. My number was", num)
            break
        else:
            guess = int(input("You are close, guess again! "))
    if guess == num:
        print("You got it! My number was", num)
    print("Thanks for playing!")

play = input("Would you like to play a guessing game? Type yes or no:")
while play == "yes":
    game()
    play = input("Would you like to play again? Type yes or no:")
print("Game Over")

