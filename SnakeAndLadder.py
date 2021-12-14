import random
size = 100

current = 1

snake = [32, 36, 48, 62, 88, 95, 97]
ladder = [1, 4, 8, 10, 28, 21, 50, 71, 88]


def checkSnake(current):
    if (current == 32):
        print("                                                     Snake")
        current = 10
    if (current == 36):
        print("                                                     Snake")
        current = 16
    if (current == 48):
        print("                                                     Snake")
        current = 26
    if (current == 62):
        print("                                                     Snake")
        current = 18
    if (current == 88):
        print("                                                     Snake")
        current = 24
    if (current == 95):
        print("                                                     Snake")
        current = 56
    if (current == 97):
        print("                                                     Snake")
        current = 78
    return current


def checkLadder(current):
    if (current == 4):
        print("                                                     Ladder")
        current = 14
    if (current == 1):
        print("                                                     Ladder")
        current = 38
    if (current == 8):
        print("                                                     Ladder")
        current = 10
    if (current == 28):
        print("                                                     Ladder")
        current = 76
    if (current == 21):
        print("                                                     Ladder")
        current = 42
    if (current == 50):
        print("                                                     Ladder")
        current = 67
    if (current == 71):
        print("                                                     Ladder")
        current = 92
    if (current == 88):
        print("                                                     Ladder")
        current = 99
    return current


tries = 0

print("Starting point: ", current, "\n\n")
key = random.randint(1, 6)
while(current <= size and current + key < size):
    key = random.randint(1, 6)
    current += key
    print("Dice: ", key)
    current = checkSnake(current)
    current = checkLadder(current)
    print("Current: ", current)
    print("\n")
    tries = tries + 1

while(current != size and current < size):
    i = random.randint(1, 6)
    print("Dice: ", i)
    if(current + i == size):
            current = current + i
            print("Current: ", current)
            break
    print("\n")
    tries = tries + 1

print("Game Done!, Your tries are: ", tries)
