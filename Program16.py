"""Write program to perform following:
     i) Check whether given number is prime or not.
    ii) Generate all the prime numbers between 1 to N where N is given number."""

# Check whether given number is prime or not.
num = input("Enter the number:")
count = 0
count1 = 0
for i in range (1,num+1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print "Given number is prime"
else:
    print "Given number is non-prime"

# Generate all the prime numbers between 1 to N where N is given number.
print "The prime numbers in between 1 and ", num, "is:"
for g in range (1,num+1):
    count1 = 0
    for j in range(1,g+1):
        if g % j == 0:
            count1 = count1 + 1
    if count1 == 2:
        print g

""" Sample o/p:
Enter the number:24
Given number is non-prime
The prime numbers in between 1 and  24 is:
2
3
5
7
11
13
17
19
23"""

