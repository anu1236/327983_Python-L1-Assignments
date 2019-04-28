"""Write a program to find the biggest of 4 numbers.
   a) Read 4 numbers from user using Input statement.
   b) extend the above program to find the biggest of 5 numbers.
(PS: Use IF and IF & Else, If and ELIf, and Nested IF)"""

max = 0
# one method
for i in range(1,5):
    n = input("Enter number")
    if n > max:
        max = n
print "Max of 4 numbers is:", max

# 2nd method

n1 = input("Enter number1:")
n2 = input("Enter number2:")
n3 = input("Enter number3:")
n4 = input("Enter number4:")
n5 = input("Enter number5:")
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print "Max is :", n1
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print "Max is :", n2
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    print "Max is :", n3
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print "Max is :", n4
else:
    print "Max is:", n5



