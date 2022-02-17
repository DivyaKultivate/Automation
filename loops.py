greeting = "Good Morning"
a = 4

if greeting == "Good Morning":
    print("Condition matches")
else:
    print("Condition does not match")
print("if else condition checked")

if greeting == "Morning":
    print("Condition matches")
else:
    print("Condition does not match")
print("if else condition checked")

if a>5:
    print("Condition true")
else:
    print("Condition false")

if a>=4:
    print("Condition true")
else:
    print("Condition false")

#For loop

obj =1, 2, 3, 4, 5
for i in obj:
    print(i)

obj1 =1, 2, 3, 4, 5
for i in obj1:
    print(i*2)

for j in range(1, 6):
    print(j*5)

#sum of First Natural Numbers 1+2+3+4+5
#range(i, j) -> i to j-i
summation = 0
for i in range(1, 6):
    summation=summation+i
print(summation)

#Example1
fruits = "Apple", "Banana", "Pomegranate"
for x in fruits:
    print(x)
    if x=="Banana":
        break

#Example2
fruits = "Apple", "Banana", "Pomegranate"
for x in fruits:
    if x=="Banana":
        print(x)
        break

#Example3
fruits = "Apple", "Banana", "Pomegranate"
for x in fruits:
    if x=="Banana":
        continue
    print(x)

#Example4
for x in range(6):
    print(x)

#Example5
for x in range(2, 6):
  print(x)

#Example6
for x in range(2, 30, 3):
  print(x)

#Example7
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Example8
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#Example9
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#Example10
for x in [0, 1, 2]:
  pass

#while
#Example2
it = 4
while it>1:
    if it != 3:
        print(it)
    it=it - 1
print("while loop execution is done")

#Example3
it = 4
while it>1:
  if it == 3:
    break
  print(it)
  it=it - 1
print("while loop execution is done")

#Example4
it = 10
while it>1:
  if it == 9:
      #it =it-1
    continue
  if it == 3:
    break
  print(it)
  it=it - 1
print("while loop execution is done")

