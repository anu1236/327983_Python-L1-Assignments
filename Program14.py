"""Write a program to create two list A &B such that List A contains Employee Id, List B contain Employee name(minimum 10 entries in each list) &perform following operation
     a) Print all names on to screen
     b) Read the index from the  user and print the corresponding name from both list.
     c) Print the names from 4th position to 9th position
     d) Print all names from 3rd position till end of the list
     e) Repeat list elements by specified number of times (N- times, where N is entered by user)
     f)  Concatenate two lists and print the output.
     g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )"""

l1 = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10"]
l2 = ["anu", "daya", "manoj", "deepa", "keerthi", "yas", "mantoo", "siva", "sudha", "anil"]

# a) Print all names on to screen
print l2

# b) Read the index from the  user and print the corresponding name from both list.
index = input("Enter the index:")
print l1[index], l2[index]

# c) Print the names from 4th position to 9th position
print l2[4:9]

# d) Print all names from 3rd position till end of the list
print l2[3:]

# e) Repeat list elements by specified number of times (N- times, where N is entered by user)
num = input("Enter number of times you want to print list")
for i in range(0,num):
    print l1

# f)  Concatenate two lists and print the output.

l3 = l1 + l2
print l3

# g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )
l4 = []
for x in range(0,len(l1)):
    l4.append(l1[x])
    l4.append(l2[x])
print l4

"""sample o/p:
['anu', 'daya', 'manoj', 'deepa', 'keerthi', 'yas', 'mantoo', 'siva', 'sudha', 'anil']
Enter the index:1
E2 daya
['keerthi', 'yas', 'mantoo', 'siva', 'sudha']
['deepa', 'keerthi', 'yas', 'mantoo', 'siva', 'sudha', 'anil']
Enter number of times you want to print list2
['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10']
['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10']
['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'anu', 'daya', 'manoj', 'deepa', 'keerthi', 'yas', 'mantoo', 'siva', 'sudha', 'anil']
['E1', 'anu', 'E2', 'daya', 'E3', 'manoj', 'E4', 'deepa', 'E5', 'keerthi', 'E6', 'yas', 'E7', 'mantoo', 'E8', 'siva', 'E9', 'sudha', 'E10', 'anil']"""