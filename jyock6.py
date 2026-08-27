# CTC389-151
# Jeff Yock
# Lab 6

stuName = ["Amy", "Billy", "Cece", "Dan", "Eddie"]

count = 0
for i in stuName:
    print(count, i)
    count = count +1

print("Menu of List Modifications")
print("Option 1 - Add Name to List")
print("Option 2 - Modify Name from List")
print("Option 3 - Delete Name from List")
optNum = int(input("Choose a numeric option from the menu above: "))

# Part 1 - Add Name

if optNum == 1:
    print("You chose to add a name")
    addName = input("Enter the new name for the list: ")
    stuName.append(addName)
    print ("Updated List")
    count = 0
    for i in stuName:
        print(count, i)
        count = count +1

# Part 2 - Modify Name

if optNum == 2:
    chgIndex1 = int(input("Choose the index number of the name to modify: "))
    print("You chose to modify name", chgIndex1)
    newName = input("Enter the new name: ")
    stuName[chgIndex1] = newName
    print ("Updated List")
    count = 0
    for i in stuName:
        print(count, i)
        count = count +1

# Part 3 - Remove Student

if optNum == 3:
    chgIndex2 = int(input("Choose the index number of the name to remove: "))
    stuName.pop(chgIndex2)
    print("You chose to remove name", chgIndex2)
    print ("Updated List")
    count = 0
    for i in stuName:
        print(count, i)
        count = count +1

