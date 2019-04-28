# Write a program to find the biggest of 3 numbers (Use If Condition)

# take 3 variables statically
a = 10
b = 5
c = 8
if a > b and a > c:
    print "The biggest number is :", a
elif b > c:
    print "The biggest number is :", b
else:
    print "The biggest number is :", c

# take 3 variables dynamically
a = input("Enter value of a:")
b = input("Enter Value of b:")
c = input("Enter Value of c:")
if a > b and a > c:
    print "The biggest number is :", a
elif b > c:
    print "The biggest number is :", b
else:
    print "The biggest number is :", c
