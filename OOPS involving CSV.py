from os import write


class Person:
    def __init__(self, name, age, m1, m2, m3):
        self.name = name
        self.age = age
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def findAverage(self):
        return (int(self.m1) + int(self.m2) + int(self.m3))/3

    def print(self):
        print(self.name, self.age, self.m1, self.m2, self.m3)


def returnPerson(temp_list):
    p = Person(temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4])
    return p

def writeTofile(fileName, P):
    file = open(fileName, "a")
    tuple = P.name, str(P.age), str(P.m1), str(P.m2), str(P.m3)
    string = (",").join(tuple) + "\n"
    file.write(string)


def printAllfromFiles(fileName):
    file = open(fileName, "r")
    listofPersonsDetails = file.readlines()
    listofPersons = []

    for strDet in listofPersonsDetails:
        temp_list = strDet.split(",")
        p = Person(temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4])
        listofPersons.append(p)

    for p in listofPersons:
        p.print()

    file.close()

def printAverageContent(fileName):
    file = open(fileName, "r")
    listofPersonsDetails = file.readlines()
    listofPersons = []

    for strDet in listofPersonsDetails:
        temp_list = strDet.split(",")
        p = Person(temp_list[0], temp_list[1], temp_list[2], temp_list[3], temp_list[4])
        listofPersons.append(p)

    for p in listofPersons:
        print(p.findAverage())

    file.close()


# main

while(1):
    print("1. Print     2. Add     3. Print Average Content     0. Exit")
    fileName = "Students.csv"
    ch = int(input("\nChoice is: "))
    if (ch == 1):
        printAllfromFiles(fileName)

    if (ch == 2):
        name = input("Name: ")
        age = int(input("Age: "))
        m1 = int(input("M1: "))
        m2 = int(input("M2: "))
        m3 = int(input("M3: "))
        list = name,age,m1,m2,m3
        p = returnPerson(list)
        writeTofile(fileName, p)

    if (ch == 3):
        printAverageContent(fileName)

    if (ch == 0):
        exit()


