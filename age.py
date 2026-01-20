import random
x=input("What is your name?: ")

while True:
    y=random.randrange(15,31)
    if input("Is your age "+str(y)+"? y/n ")=="y":
        print(x+" is "+str(y)+" years old.")
        break
    else:
        print("Rats")
    
    