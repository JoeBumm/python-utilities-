import os
import math
def lines(i):
    i = 0
    while i<5: 
        print("....................")
        i+=1

print("This tool will make you schedule shutdowns!")
print("Please Choose when do you want to schedule (Write in minutes) ")
lines(1)
x = int(input("Enter: "))

while (x<0 or x>6000):
    print("Enter a suitable time")
    x = int(input("Enter: "))








    

