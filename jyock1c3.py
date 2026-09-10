# CTC389-151
# Jeff Yock
# Lab 1c v3 (re-resubmit)
# Fahrenheit to Celsius

def f_to_c(fahr):
    cel = (fahr - 32) * (5 / 9)
    return cel

print ("This program will convert Fahrenheit to Celsius.")
userDegF = int(input("Enter an integer temperature value in Fahrenheit: "))

print("You entered",userDegF,"degrees Farenheit.")
    
userDegC = f_to_c(userDegF)
print("The temperature in Celsius is", int(userDegC) ,"degrees.")

