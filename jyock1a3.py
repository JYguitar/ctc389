# CTC389-151
# Jeff Yock
# Lab 1a v3 (re-resubmit)
# Part 1

guess = 0
num = 4
print("Let's play a guessing game!")
print ("I have selected a number between 1 and 10 ")
guess = int(input("Guess my number! "))
while guess!= num:
    guess = int(input("Sorry, that is not my number. Guess again! "))
print("Hooray! You win! My number was", num)
print("Thanks for playing!")

