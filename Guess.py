import random as rand

print("***          Welcome to the Guessing Game by Rohith Boppey!          ***\n\n\n")
ch = int(input("Do you want to start the game: "))
while(ch != 0):
    number = rand.randrange(1, 10000)
    ou = 0,
    n = 0
    while(ou != number):
        ou = int(input("Your number is: "))
        if(ou < number):
            print("Number greater than", ou, "\n")
        else:
            print("Number less than", ou, "\n")
    print("\nDamn! You found the number is found\n")
    ch = int(input("Do you want to continue: "))
print("\nThank you for playing with me!\n\n")
  