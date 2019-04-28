"""Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1 (reverse printing)
a) By using For loop
b) By using while loop
c) Let mystring ="Hello world"
print each character of mystring in to separate line using appropriate loop structure."""

# a) By using For loop
for i in range (1, 101):
    print i

for i in range(100, 0, -1):
    print i

# b) By using while loop
print "In while loop\n"
i = 1
while i <= 100:
    print i
    i = i + 1

i = 100
while i > 0:
    print i
    i = i - 1

# c) Let mystring ="Hello world" print each character of mystring in to separate line using appropriate loop structure.

string = "Hello world"
for i in range(0,len(string)):
    print string[i]+"\n"
