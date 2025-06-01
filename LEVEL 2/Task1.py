import random
x=int(input("Guess the number between 1 and 100:"))
target=random.randint(1,100)
while True:
    if x==target:
        break
    elif x<target:
        print("Too Low! Try again")
    else:
        print("Too High! Try again") 
print("You guessed the correct number",target)  
