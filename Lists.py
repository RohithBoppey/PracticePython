# Give the sum of the numbers as an other list and Strings as a string seperated by space

list1 = [1, 2, 34, 45, 67, "Python", "is", "a", "great", "language"]
print(type(list1[1]))
int_list = []
str_list = []

# int_list = [e for e in list1 if type(e) == int]

for i in list1:
    if(type(i) == str):
        str_list.append(i)
    elif(type(i) == int):
        int_list.append(i)

print(int_list)
print(str_list)
s = (" ").join(str_list)
print(s)

# For copying dont use l2 = l1, instead:

l2 = list1.copy()

# now both have individual list and one doesn't affects the elements of another

# for update and delete -> pop, remove, clear and  del

r = l2.pop()
l2.remove("Python")
print(l2, r)
l2.clear # entire list is truncated, del to delete the list with variable as well
del str_list
int_list.sort()
print(int_list)

# reverse for reverse thing
