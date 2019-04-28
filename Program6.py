"""Write a program to read string and print each character separately.
    a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
    b) Repeat the string 100 times using repeat operator *
    c) Read string 2 and concatenate with other string using + operator."""

string1 = raw_input("Enter the string:")
print string1
for x in range(len(string1)):
    print string1[x]

# Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
print string1[4:6]
print string1[7:]

# Repeat the string 100 times using repeat operator *
string1 = string1+' '
print (string1 * 100)

# Read string 2 and concatenate with other string using + operator.
string2 = raw_input("Enter the string:")
string = string1 + string2
print string

"""Sample o/p:
Enter the string:anu is good
anu is good
a
n
u

i
s

g
o
o
d

is
good
anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good anu is good
Enter the string:programmer
anu is good programmer"""
