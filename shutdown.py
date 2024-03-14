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

print("type 1 for instant shutdown")
print("type 2 for 60 minutes")
print("type 3 for 2 hours")
print("type 4 for 3 hours")

x = int(input("Enter: "))

while (x<0 or x>6000):
    print("Enter a suitable time")
    x = int(input("Enter: "))

def scheduler
if x==1:
    os.system("shutdown /t /s 1")
if x==2:
    os.system("shutdown /t /s 3600")
if x==3:
    os.system("shutdown /t /s 7200")
if x==4:
    os.system("shutdown /t /s 14400")







    

