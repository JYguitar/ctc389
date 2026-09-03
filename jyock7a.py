# CTC389-151
# Jeff Yock
# Lab 7
# Part 1

num = 5

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

