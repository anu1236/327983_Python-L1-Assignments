# Write a program to find the number is Prime or not.

# prime number is a number is divded by 1 and itself
num = input("Enter a number:")
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count = count + 1
    print count

if (count == 2):
    print "Given number is prime"
else:
    print "Given number is non-prime"
    