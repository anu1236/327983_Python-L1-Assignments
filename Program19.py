"""Using loop structures print even numbers between 1 to 100.
a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
    i) Break the loop if the value is 50
    ii) Use continue for the values 10,20,30,40,50
      b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
      i) Break the loop if the value is 90
      ii) Use continue for the values 60,70,80,90

a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
    i) Break the loop if the value is 50
    ii) Use continue for the values 10,20,30,40,50"""

for x in range(1, 100):
    if x == 50:
        break
    if x in [10, 20, 30, 40, 50]:
        continue
    if x % 2 == 0:
        print x

# By using while loop, use continue/ break/ pass statement to skip odd numbers.

y = 1
while y < 100:
    y += 1
    if y == 90:
        break
    if y in [60, 70, 80, 90]:
        continue
    if y % 2 == 0:
        print y
