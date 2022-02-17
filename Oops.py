#Ex1
class Calculator:
    num = 100

    def getData(self):
        print("I am now executing as method in class")

calc = Calculator()  #syntax for create object in python
calc.getData()
print(calc.num)
print("---------------------------------------")

#Ex2
# self keyword is mandatory for calling variable names into method
# Instance and class variable have whole different purpose
# constructor name should be __Init__
# new keyword is not required when you create object

class Calculator:
    num = 100  #class variable

    # default constructor
    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num

calc = Calculator(2, 3)
calc.getData()
print(calc.summation())

calc = Calculator(4, 5)  
calc.getData()
print(calc.summation())
print("---------------------------------------")


