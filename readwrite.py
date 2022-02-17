file = open('test.txt')
# Read all the contents of file
# Read n number of characters by passing parameters

#print(file.read())
#print(file.read(7))

# Read one single line at a time readline()
#print(file.readline())
#print(file.readline())

# Print line by line using readline menthod
#line = file.readline()
#while line!="":
#    print(line)
#    line = file.readline()
#line = ['apple', 'bag', 'cat', 'dog', 'elephant', 'fog']
for line in file.readlines():
    print(line)
file.close()
#print(line)