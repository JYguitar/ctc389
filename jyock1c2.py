# CTC389-151
# Jeff Yock
# Lab 1c v2 (resubmit)
# Fahrenheit to Celsius

def f_to_c(f):
    c = (f - 32) * (5 / 9)
    return c

print ("This program will convert Fahrenheit to Celsius.")
f = int(input("Enter an integer temperature value in Fahrenheit: "))

print("You entered",f,"degrees Farenheit.")
    
c = f_to_c(f)
print("The temperature in Celsius is", int(c) ,"degrees.")

