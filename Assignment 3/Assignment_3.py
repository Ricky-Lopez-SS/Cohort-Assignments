
import random

def divBy7And5():

    retList = []
    for i in range(1500, 2701):
        if( not(i % 7) and not(i % 5)): #truthiness
            retList.append(i)
    return retList

def toFahrenheit(celsius):
    return (celsius * 1.8) + 32

def toCelsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

def numberGuesser():
    number = random.randint(1, 10)
    guess = 0
    while number != guess:
        guess = int(input("Please guess a number between 1 and 10. ") )

    print("Well guessed!")

def stars():

    for i in range(6):
        for k in range(i):
            print('* ' , end='')
        print()

    for i in range(4, 0, -1):
        for k in range(i):
            print('* ', end='')
        print()

def reverse(word):
    print("Reversed word is: {}".format(word[::-1]) )

def oddsAndEvens(nums):

    evenCounter = oddCounter = 0


    
    for num in nums:
        if(num % 2): #is odd.
            oddCounter += 1
        else:
            evenCounter += 1

    return oddCounter, evenCounter

def types(item_list):

    return [(type(i), i) for i in item_list]

def three_to_six():
    for i in range(7):
        if(i == 3 or i == 6):
            continue
        print("{}  ".format(i) , end='')


if __name__ == '__main__' :

    print("Question 1\n\n")

    print("Values between 1500 and 2700 that are divisible by 5 and 7: {}".format(divBy7And5()) )

    print("\n\nQuestion 2\n\n")

    temperatureType = input("Please enter the temperature type you would like to convert from: ")
    temperature = float(input("Please enter the temperature you would like to convert: "))

    if(temperatureType.lower() == 'fahrenheit'):
        print("The temperature in celsius is: {}".format(toCelsius(temperature)) )
    elif(temperatureType.lower() == 'celsius'):
        print("The temperatire in fahrenheit is: {}".format(toFahrenheit(temperature)) )
    else:
        print("Sorry, the input was invalid. Please restart the program and try again.")

    print("\n\nQuestion 3\n\n")

    numberGuesser()

    print("\n\nQuestion 4\n\n")

    stars()

    print("\n\nQuestion 5\n\n")

    reverse(input("Please enter a string you would like to reverse: "))

    print("\n\nQuestion 6\n\n")

    nums = input("Please enter a string of comma-separated numbers: ")

    nums = [ int(i) for i in nums.split(',') ]

    oddsEvens = oddsAndEvens(nums)

    print("Number of odds: {0}\nNumber of evens: {1}".format(oddsEvens[0], oddsEvens[1]) )

    print("\n\nQuestion 7\n\n")

    dataList = types( [1452, 11.23, 1+1j, True, 'w3resource', (0, -1), [5,12], {"class":'V', "section":'aA'}] )
    
    print("datatypes for example list: \n\n")

    for i in dataList:
        print("{}\n".format(i))

    print("\n\nQuestion 8\n\n")

    three_to_six()

    print()










