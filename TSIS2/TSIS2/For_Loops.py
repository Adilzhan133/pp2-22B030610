#For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping Through a String
for x in "banana":
  print(x)

#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range() Function ()
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)

#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)

#Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 

#The pass Statement
for x in [0, 1, 2]:
  pass