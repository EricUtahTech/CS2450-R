import random
x=input("What is your name?: ")
low=15
high=31
while True:
    y=random.randrange(low,high)
    z=input("Is your age "+str(y)+"? y for yes, h for too high, l for too low: ")
    if z=="y":
        print(x+" is "+str(y)+" years old.")
        break
    elif z=="h":
        high=y
        print("Rats, let's try again...")
    elif z=="l":
        low=y+1
        print("Rats, let's try again...")
    
    