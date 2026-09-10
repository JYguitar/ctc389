# CTC389-151
# Jeff Yock
# Lab 1b v3 (re-resubmit)
# Volume of a Cylinder

def cylvol(rad,hgt):
    vol = 3.14159 * (rad**2) * hgt
    return vol

print ("This program calculates the volume of a cylinder given the radius and height.")
userRad = float(input("Enter a positive value for your radius: "))
userHgt = float(input("Enter a positive value for your height: "))
print("You entered a radius of", userRad, "and a height of", userHgt)
yourVol = cylvol(userRad,userHgt)
print("Your cylinder's volume is", yourVol ,"units.")

