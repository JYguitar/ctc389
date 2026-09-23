# CTC389-151
# Jeff Yock
# Lab 8

qstn1 = ["Study for the test", "Play video games", "Watch TV"]
ansr1a = ["You feel tired but you know the test is important.", "You deserve a break!", "Your hear the theme song from your favorite TV show."]
ansr1b = ["You study a little before bed.", "You play video games until midnight.", "You go to the family room and watch TV before bed."]

qstn2 = ["Study a litte more before school.", "Pretend to be sick.", "Make a plan to cheat."]
ansr2a = ["You decide it might be a good idea to review more before school.", "You burp the smelliest burp you can burp.", "It's too late to study now."]
ansr2b = ["You study a little at breakfast and in the car.", "Then you moan 'Mom. I dont feel so good.'", "You heard there's a kid at school that sells test answers."]

qstn3 = ["Buy the cheat sheet.", "Say 'No thanks' and walk to class.", "Warn the teacher about the cheat sheet."]
ansr3a = ["The kid says 'Five bucks, pal.'", "You shake your head, say 'No thanks,' and hurry to class.", "You hurry to the classroom and tell your teacher what happened."]
ansr3b = ["You think it's too much money but buy it anyway.", "The kid laughs and says 'OK, enjoy your F!'", "She thanks you and says 'Hmmm, I think those cheaters will get a little surprise today.'"]

qstn4 = ["Try to help.", "Watch and laugh.", "Go to a different bathroom."]
ansr4a = ["You feel afraid but want to help. You say 'Stop!' and start running to go tell an adult.", "You always wanted big friends. They seem so cool.", "You feel bad but don't want any more problems today."]
ansr4b = ["The big kids get worried, let the kid go, and run off in the other direction.", "You start laughing too and ask if you can help flush.", "You pretend you didn't see or hear anything and walk away."]

qstn5 = ["Peek at your neighbor's test.", "Try doing the math problem on scratch paper.", "Just guess."]
ansr5a = ["Your desk partner finished his test super fast and is smiling the biggest smile.", "You decide to try modeling the problems on scratch paper. It really helps!", "You're totally lost on this test and regret not studying."]
ansr5b = ["He didn't cover his paper and you decide to copy all of his answers.", "You remember how to solve these kinds of problems and finish just in time.", "You just cross you fingers and start guessing."]

def firstQ (sentName):
  print(" ")
  print(sentName, "you had a long hard day at school.")
  print("It's Thursday night and you have one day left before the weekend.")
  print("But you know that Friday is test day.")
  print("You should study but you feel super tired.")
  print("What should you do?")
  count = 1
  for i in qstn1:
    print(count, i)
    count = count + 1
  choice = int(input("Enter 1, 2, or 3: "))
  choice = choice - 1
  print(ansr1a[choice])
  print(ansr1b[choice])
  choice = choice + 1
  if choice == 1:
      points1 = 30
  elif choice == 2:
      points1 = -10
  elif choice == 3:
      points1 = 0
  return (points1)
  
def secondQ (sentName):
  print(" ")
  print("You hear your mom calling.", sentName, "wake up! It's time for school.")
  print("You quickly get dressed but feel worried about your test")
  print("Maybe you could study a little more.")
  print("Or maybe it's time for a new plan.")
  print("What should you do?")
  count = 1
  for i in qstn2:
    print(count, i)
    count = count + 1
  choice = int(input("Enter 1, 2, or 3: "))
  choice = choice - 1
  print(ansr2a[choice])
  print(ansr2b[choice])
  choice = choice + 1
  if choice == 1:
      points2 = 20
  elif choice == 2:
      print("Your mom feels your forehead, and decides to take you to the doctor.")
      print("The doctor gives you a PAINFUL SHOT with a GIANT NEEDLE!")
      print("Now you REALLY feel sick.")
      points2 = -500
  elif choice == 3:
      points2 = -30
  return (points2)

def thirdQ (sentName):
  print(" ")
  print("When you get to school lots of kids are hanging out waiting for the gate to open.")
  print("One of the older kids sees you and walks over.")
  print("He says, 'Hey", sentName, "do you wanna buy the answers for your Math test today?'")
  print("What should you do?")
  count = 1
  for i in qstn3:
    print(count, i)
    count = count + 1
  choice = int(input("Enter 1, 2, or 3: "))
  choice = choice - 1
  print(ansr3a[choice])
  print(ansr3b[choice])
  choice = choice + 1
  if choice == 1:
      print("As soon start looking at the test answers, you feel a tap on your shoulder.")
      print("You turn around and it's the PRINCIPAL!")
      print("He takes the you and the cheat sheet straight to his office and CALLS YOUR MOM!")
      points3 = -500
  elif choice == 2:
      points3 = 10
  elif choice == 3:
      points3 = 20
  return (points3)

def fourthQ (sentName):
  print(" ")
  print("You still feel nervous about the test so you ask if you can use the restroom first.")
  print("The teacher says, 'OK", sentName, "but be quick. We are about to start the test.")
  print("You hurry out to the closest restroom but when you go in you see three older kids bullying a little kid.")
  print("They are trying to put him into the toilet. They are laughing so hard they dont see you.")
  print("What should you do?")
  count = 1
  for i in qstn4:
    print(count, i)
    count = count + 1
  choice = int(input("Enter 1, 2, or 3: "))
  choice = choice - 1
  print(ansr4a[choice])
  print(ansr4b[choice])
  choice = choice + 1
  if choice == 1:
      points4 = 10
  elif choice == 2:
      print("With all the laughing you don't notice the school safety officer come into the restroom.")
      print("You and all the big kids get SUSPENDED FOR BULLYING!")
      print("Your parents are VERY ANGRY and DISAPPOINTED.")
      points4 = -500
  elif choice == 3:
      points4 = 0
  return (points4)
  
def fifthQ (sentName):
  print(" ")
  print("It's finally time for the Math test.")
  print("You write", sentName, "on the top of your paper and begin.")
  print("It starts out easy but gets harder and harder.")
  print("You get stuck on a few problems and time is running out.")
  print("What should you do?")
  count = 1
  for i in qstn5:
    print(count, i)
    count = count + 1
  choice = int(input("Enter 1, 2, or 3: "))
  choice = choice - 1
  print(ansr5a[choice])
  print(ansr5b[choice])
  choice = choice + 1
  if choice == 1:
      print("After the test, the teacher announces she had heard there was a cheat sheet being sold on campus.")
      print("So she changed all the answers so anyone who used it would get every question wrong instead!")
      print("Your neighbor stops smiling and starts crying. They used the cheat sheet and know they got a ZERO!")
      print("And since you copied him... SO DID YOU!")
      points5 = -500
  elif choice == 2:
      points5 = 20
  elif choice == 3:
      points5 = -20
  return (points5)

def results(score):
  if score == 100:
    print("Your grade is A+ and you made great choices today")
    print("You truly are the BEST STUDENT EVER!")
    print("Congratulations, you got the best ending!")
  elif score == 90:
    print("Your grade is A")
    print("So close! You did very good today but there is one better ending.")
  elif score == 80:
    print("Your grade is B")
    print("You did good today but there are better endings.")
  elif score == 70:
    print("Your grade is C")
    print("You did OK today but you should try again.")
  elif score == 60:
    print("Your grade is D")
    print("You barely passed! You should definitely try again.")
  elif score < 60:
    print("Your grade is F! You need to think about your choices. Try again!")
 
  

play = input("Would you like to play a super cool interactive story? Type yes or no: ")
if play == "no":
    print("Too bad, but you would probably lose anyway!")
else:
   while play == "yes":  
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = 0
    score5 = 0
    scoreTot = 0
    print(" ")
    print ("Great! this game is called Best Student Ever.")
    print ("I will tell you a story but sometimes you can choose what to do.")
    print ("Be careful though, some choices are good but some are bad.")
    print(" ")
    plyrName = input("First of all, type in your game name: ")
    print("OK, let's begin!")
    print(" ")
    score1 = firstQ(plyrName)
    score2 = secondQ(plyrName)
    if score2 > -100:
      score3 = thirdQ(plyrName)
      if score3 > -100:
        score4 = fourthQ(plyrName)
        if score4 > -100:
          score5 = fifthQ(plyrName)
          scoreTot = scoreTot + score1 + score2 + score3 + score4 + score5
          if scoreTot < 0:
            scoreTot = 0
          print(" ")
          print ("The teacher says,'I have graded all the tests.'")
          print (plyrName, "your test score is", scoreTot)
          results(scoreTot)
          print(" ")
    play = input("Would you like to play again? Type yes or no: ")
print("Game Over")



