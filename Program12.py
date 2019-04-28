"""Read 10 numbers from user and find the average of all.
a) Use comparison operator to check how many numbers are less than average and print them
b) Check how many numbers are more than average.
c) How many are equal to average."""

arr = []
sum = average = 0
n = input ("How many numbers you will enter:")
for i in range(n):
    num = input("Enter the number")
    arr.append(num)
    sum = sum + arr[i]
    average = sum / n;
print sum,average

# Use comparison operator to check how many numbers are less than average and print them
count = 0
for i in range(n):
    if arr[i] < average:
        count +=1
        print arr[i]
print "less than average", count

# Check how many numbers are more than average.
count = 0
for i in range(n):
    if arr[i] > average:
        count +=1
print "numbers are more than average", count

# How many are equal to average.
count = 0
for i in range(n):
    if arr[i] == average:
        count+=1
print "equal to average", count

"""o/p:
How many numbers you will enter:5
Enter the number1
Enter the number2
Enter the number3
Enter the number4
Enter the number5
15 3
1
2
less than average 2
numbers are more than average 2
equal to average 1"""