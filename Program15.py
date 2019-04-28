"""Create a list of 5 names and check given name exist in the List.
        a) Use membership operator (IN) to check the presence of an element.
        b) Perform above task without using membership operator.
        c) Print the elements of the list in reverse direction."""

l = ['anu', 'anusha', 'sneha', 'kumar', 'pinky']

# a) Use membership operator (IN) to check the presence of an element.
name = raw_input("Enter the name you want to check:")
if name in l:
    print name, "Exists in list"
else:
    print name, "doesn't exist"

# b) Perform above task without using membership operator.
flag = 0
for x in range(len(l)):
    if l[x] == name:
        flag = 1
        print name, "Exists in list"
        break
if flag == 0:
    print name, "doesn't exist"

# c) Print the elements of the list in reverse direction.
l2 = []
print l[::-1]
for x in range(len(l)-1,0,-1):
    l2.append(l[x])
print l2

"""sample o/p:
Enter the name you want to check:anu
anu Exists in list
anu Exists in list
['pinky', 'kumar', 'sneha', 'anusha', 'anu']"""
