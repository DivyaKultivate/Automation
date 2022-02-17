
#Numeric
#create a variable with integer value.
a=100
print("The type of variable having value", a, " is ", type(a))

#create a variable with float value.
b=10.2345
print("The type of variable having value", b, " is ", type(b))

#create a variable with complex value.
c=100+3j
print("The type of variable having value", c, " is ", type(c))


#String
a = "string in a double quote"
b= 'string in a single quote'
c=5
print(a)
print(b)

# using ',' to concatenate the two or several strings
print(a, "concatenated with", b)
print(a, "concatenated with", b, c)

#using '+' to concate the two or several strings
print(a+" concated with "+b)

#List
#list of having only integers
a= [1,2,3,4,5,6]
print(a)

#list of having only strings
b=["hello","john","reese"]
print(b)

#list of having both integers and strings
c= ["hey","you",1,2,3,"go"]
print(c)

#index are 0 based. this will print a single character
print(c[1]) #this will print "you" in list c

a=[1, 2, "Hello World", 4, 5]
print(a[-1]) #print Last value

print(a[2:4])

a.append("Thank you") #Add the character
print(a)
a.insert(4, "Test")
print(a)

a[2]="Party"  #Updating
print(a)

del a[0] #deleting
print(a)

#Tuple
#tuple having only integer type of data. Data given within Open brackets
a=(1,2,3,4)
print(a) #prints the whole tuple
b=("test1", "test2", 5, 4.5)
print(b[2])

#tuple having multiple type of data.
b=("hello", 1,2,3,"go")
print(b) #prints the whole tuple

#index of tuples are also 0 based.

print(b[4]) #this prints a single element in a tuple, in this case "go"

#Dictionary
#a sample dictionary variable

a = {1:"first name","Name":"last name", "age":33}

#print value having key=1
print(a[1])
#print value having key=2
print(a["Name"])
#print value having key="age"
print(a["age"])

dict = {}

dict["firstname"]="Divya"
dict["lastname"]="Priya"
dict["gender"]="female"

print(dict)
print(dict["lastname"])







