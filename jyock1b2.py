# CTC389-151
# Jeff Yock
# Lab 1b v2 (resubmit)
# Volume of a Cylinder

def cylvol(r,h):
    v = 3.14159 * (r**2) * h
    return v

print ("This program calculates the volume of a cylinder given the radius and height.")
r = float(input("Enter a positive value for your radius: "))
h = float(input("Enter a positive value for your height: "))
print("You entered a radius of", r, "and a height of", h)
v = cylvol(r,h)
print("Your cylinder's volume is", v ,"units.")

