
def divBy7Not5():

    retList = []
    for i in range(2000, 3201):
        if( not(i % 7) and (i % 5)): #truthiness
            retList.append(i)
    return retList

def factorial(num):
    
    sum = 1

    for i in range(num):
       sum *= i+1

    return sum

def squares(num):
    
    squares = {}

    for i in range(1, num+1):
        squares[i] = i*i
    
    return squares

def toList(values):

    return values.split(",")


class ClassExample() :

    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = input("Please enter the string you would like to instantiate the class with: ")

    def printString(self):
        print(self.str.upper())




if __name__ == '__main__' :

   print("Coding Exercise 4\n")

   listEx = [4, 'word' , 3.6]

   print("%s\n" %(listEx) ) 

   #I assume this is what the assignment meant with the second list, as the example shown in the assignment yields an error.
   listEx2 = [1, 1, [1,2]]

   print("Grabbing the value of 2 from the nested list: %s\n" %(listEx2[2][1]) )

   lst = ['a', 'b', 'c']

   print("lst[1:] is %s\n" %(lst[1:]))

   dictEx = {'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}

   print("dictionary: %s\n" %(dictEx)) 

   D = {'k1':[1,2,3]}

   print("The output of D[k1][1] is normally an error, but if you were to format it properly, it would be: %s\n" %(D['k1'][1])  )

   tupleEx = tuple([1,[2,3]])

   print("Yes, the tuple for the requested list would be: {0}\n".format(tupleEx) )

   print("Yes, creating the distinct character word from the set: ", end="")

   setEx = set('Mississippi')

   for i in setEx:
       print(i, end='')

   print("\n")

   setEx.add('X')

   print("Yes you can add the character 'X'. The new set is now: ", end="")

   for i in setEx:
       print(i, end="")

   print("\n")

   print("{0}".format(set([1,1,2,3])) )

   print("\nProgramming Question 1\n\n")

   print("Valid numbers between 2000 and 3200:\n\n")

   for i in divBy7Not5():
       print("{0}, ".format(i) , end="")
   

   print("\n\nProgramming Question 2\n\n")

   inputValue = int(input("Please input a value in order to find its factorial: "))
   
   print("\n\nThe factorial of this value is: {0}".format(factorial(inputValue))  )

   print("\n\nProgramming Question 3\n\n")

   inputValue = int(input("Please input a value for the squares dictionary: "))

   print(squares(inputValue))

   print("\n\nProgramming Question 4\n\n")

   inputValue = input("Please input a comma-separated string of numbers to construct a list and a tuple: ")

   finalList = toList(inputValue)

   print("\n\nlist: {0}\ntuple: {1}".format(finalList, tuple(finalList))  )

   print("\n\nProgramming Question 5\n\n")

   classEx = ClassExample()
   classEx.getString()
   classEx.printString()



