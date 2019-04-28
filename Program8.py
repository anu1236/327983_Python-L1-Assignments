"""Create a tuple with at least 10 elements having integer values in it;
       Print all elements
       Perform slicing operations
       Perform repetition with * operator
       Perform concatenation with other tuple."""

t = (102, 20, 56, 12, 36, 27, 8, 11, 21, 15)
# Print all elements
for x in range(len(t)):
    print t[x]

# Perform slicing operations
print t[1:5]
x = slice(2)
print t[x]
print t[6:]
print t[1:6:2]
print t[::-1]

# Perform repetition with * operator
print t * 2

# Perform concatenation with other list.
t2 = (23, 88)
t3 = t + t2
print t3