#Ex1
def GreetMe():
    print("Good Morning")

GreetMe()

#Ex2
def GreetMe(name):
    print("Good Morning" + name)

GreetMe("Divya")

#Ex3
def GreetMe(name):
    print("Good Morning" + name)

def AddIntegers(a, b):
    print(a+b)

GreetMe("Divya")

AddIntegers(4, 5)

#Ex4
def GreetMe(name):
    print("Good Morning" + name)

def AddIntegers(a, b):
    return a+b

GreetMe("Divya")

print(AddIntegers(4, 5))