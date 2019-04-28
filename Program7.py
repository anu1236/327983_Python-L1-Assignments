"""Create a list with at least 10 elements having integer values in it;
       Print all elements
       Perform slicing operations
       Perform repetition with * operator
       Perform concatenation with other list."""

l = [102, 20, 56, 12, 36, 27, 8, 11, 21, 15]
# Print all elements
for x in range(len(l)):
    print l[x]

# Perform slicing operations
print l[1:5]
print l[6:]
print l[1:6:2]
print l[::-1]

# Perform repetition with * operator
print l * 2

# Perform concatenation with other list.
l2 = [23, 88]
l3 = l + l2
print l3