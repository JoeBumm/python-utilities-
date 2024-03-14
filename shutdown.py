import os

def lines(i):
    for _ in range(i):
        print("....................")

print("This tool will help you schedule shutdowns!")
print("Please choose when you want to schedule")
lines(1)

print("Type 1 for instant shutdown")
print("Type 2 for 60 minutes")
print("Type 3 for 2 hours")
print("Type 4 for 3 hours")

x = int(input("Enter: "))

while x < 0 or x > 6000:
    print("Enter a suitable time")
    x = int(input("Enter: "))

def sup(x):
    if x == 1:
        os.system("shutdown /s /t 1")
    elif x == 2:
        os.system("shutdown /s /t 3600")
    elif x == 3:
        os.system("shutdown /s /t 7200")
    elif x == 4:
        os.system("shutdown /s /t 14400")
    else:
        print("This option does not exist")

flag = False
sup(x)

if not flag:
    print("Your shutdown is scheduled.")
else:
    print("Please rerun the program.")
