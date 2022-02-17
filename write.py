# Read the file and store all the lines in list
# Reverse the list
# write the list bact to the file
#Ex1

with open('test.txt','r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)

#Ex2
f = open("test.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("test.txt", "r")
print(f.read())

#Ex3
#Create a new file myfile.txt
#f = open("myfile.txt", "x")

# Write a file
f = open("myfile.txt", "w")
f.write("Write a data in a file")
f.close()

#Ex4
# Deleting a file
#import os
#os.remove("myfile.txt")

#Check if File exist:
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file doesn't exist")










