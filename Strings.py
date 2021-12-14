# There are multiple operations on string

# 1. Indexing s[0], s[1], etc
# 2. Slicing s[0:5]. s[:6]
# 3. Striding s[0::2] Start from index 0 and print every 2nd char

s = "Python is good"

print(s[2]) #indexing
print(s[0:6], " *one word done* ", s[7:]) #slicing
print(s[0::2]) #striding

#  Placeholder in python looks like {............}

num1 = 10
num2 = 20

# Possible ways are: 

s = "the given values are {} and {}".format(num1, num2)
s1 = "The given values are {1} and {0}".format(num1, num2)
s2 = "The given values are {val1} and {val2}".format(val1= num1, val2 = num2)
print(s)
print(s1)
print(s2)

# other string functions

s = s.capitalize() #Capitalises the first sentence 
print(s)
print(s.upper())
print(s.lower())
print(s.title()) # This makes the first letter of all words captialised

# To check true or false, we can use
print(s.isupper())

# Splitting the .csv string and seperating as strings
str = "CSV,CSS,PYTHON,JAVA,Django"
str_list = str.split(",")
print(str_list)

# Making the ones in lowercase to lowercase and the mixed one to upper case
for i in range(len(str_list)):
    if str_list[i].isupper():
        str_list[i] = str_list[i].lower()
    elif str_list[i].istitle():
        str_list[i] = str_list[i].upper()

# One way to return the new list is by 

finalNewString = (",").join(str_list)
print(finalNewString)

# replacing words in string using maketrans and translate

s1 = "abcd"
s2 = "1234"

s3 = "Python is the new abcd"

# Creating a mapping table first and then mapping accordingly

t = ""
table = t.maketrans(s1, s2)
s3 = s3.translate(table)
print(s3)

#removing white spaces before the string and after the string can be done as strip

st = "                       Hello World                            "
s4 = st.strip(" ")
print(s4)