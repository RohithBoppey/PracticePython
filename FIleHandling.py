
# reading file -> .read() reads entirely and gives us .readline() reads only one line, .readlines() reads all lines and returns a list of Strings

file = open("filetoread.txt", "r")
x = file.read()
print(x)
file.close()

#writing a file

import datetime

file = open("filetowrite.txt", "w")
x = datetime.datetime.now()
s = x.strftime("%b %d %Y %H:%M:%S")
string = "This file is being written at "+ s
file.write(string)
file.close()