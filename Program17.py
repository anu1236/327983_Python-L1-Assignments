"""Write program to find the biggest and Smallest of N numbers.
      PS: Use the functions to find biggest and smallest numbers. """

#def biggest():

l = []
N = input("How many numbers do you want to enter:")
for i in range(0,N):
    num = input("Enter the number:")
    l.append(num)
print l

print "biggest number is: ", max(l)
print "smallest number is : ", min(l)

"""Sample o/p:
How many numbers do you want to enter:2
Enter the number:11
Enter the number:2
[11, 2]
biggest number is:  11
smallest number is :  2"""