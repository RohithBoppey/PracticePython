#for loop for printing elements of the list

from typing import Sized


list = [1,4,5,6,2,4,5,6]
print("General List print: ", end = "")
print(list)
print("Printing using for loop: ", end=" ")

for i in list:
    print(i, end = " ")

print("\n\nFinding sum Using While loop: ", end=" ")
i = 0
sum = 0
while i < len(list):
    sum = sum + list[i]
    i= i + 1

print(sum)

print("\nFinding sum Using For loop: ", end=" ")
sum = 0
for i in list:
    sum = sum + i
print(sum)

# Using the range function as needed: 3 types
# 1. range(5) = 0 1 2 3 4 
# 2. range(5,10) = 5, 6, 7, 8, 9
# 3. range(5, 100, 5) = 5 10 15 20 ....... 95

print("Using the range and loops to print values")
print("1. Using normal range i.e. range(10): ")

for i in range(10):
    print(i, end = " ")

print("\n\n2. Using range(5, 10): ")

for i in range(5, 10):
    print(i, end = " ")

print("\n\n3. Using ranged step (5, 100, 10): ")

for i in range(5, 100, 10):
    print(i, end = " ")

# saving the result in the list
print("\n\nAdding it to a list: ")
list = []
for i in range(1, 101):
    if(i % 4 == 0):
        list.append(i)
    
print(list, len(list))

#enumerate in python -> gives us the index and python:

# for index, value in enumerate(list):
#     print(index, " ", value)




