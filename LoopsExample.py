# Q1: Give a list which is divisible by 7 and 5 for numbers between 1500 and 2700:

list = []
for i in range(1500,2701):
    if(i % 5 == 0 and i % 7 == 0):
        list.append(i)
print(list)

# Q2: Give a count of even and odd numbers in 1 to 9:

even_count = 0
odd_count = 0

for i in range(1, 10):
    if(i % 2 == 0):
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print(even_count, " ", odd_count)        

# Q3: Using loops and if conditions:

for i in range(1, 25):
    # print(i)
    if (i % 3 == 0):
        print("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")

# Q4: Factorial of a number: 

i = 5
p = 1
while i != 0:
    p = p * i
    i = i - 1
print(p)


