#Ex1
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print("Ex1-----------------------------")

#Ex2
#A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type.
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

print(myvar[1]) # Return the first value of the Series

#print(pd.__version__)
print("Ex2-----------------------------")

#Ex3
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
print("Ex3-----------------------------")

#Ex4
#dictionary with series
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)
#myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
print("Ex4-----------------------------")

#Ex5
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
print("Ex5-----------------------------")

#Ex6
#Example for DataFrame
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)
print(df.loc[0])
print(df.loc[[0, 1]])
print("Ex6-----------------------------")

#Ex7
#Named Index
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)
print(df.loc["day2"])
print("Ex7-----------------------------")

#Ex8
import pandas as pd

df = pd.read_csv('input_file.csv')

print(df)
print("Ex8-----------------------------")




