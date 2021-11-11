import string


def isPalindrome(word) :

    word = word.lower()

    for i in (string.punctuation + ' '):
        word = word.replace(i, '')

    for i in range(len(word)):

        if word[i] != word[-(i+1)]:
            return "N"

    return "Y"



if __name__ == '__main__' :

    print("Coding Exercise 3\n")

    print("%s\n" %("Hello World"[8]) )

    print("%s\n" %("thinker"[2:5]) ) 

    #The output of h[1] given S = 'hello' is a name error, as h has not been initialized

    #The output of s[2:] given S = 'Sammy" is a name error, as s has not been initialized

    x = set('Mississipi')

    [print(i, end='') for i in x]

    print("\n\n***********************************")

    print('\nPalindrome Exercise\n\n')

    numOfStrings = int(input("Please input the number of strings for the palindrome test, followed by each string.\n") )

    returnString = ""

    for i in range(numOfStrings):
        returnString += isPalindrome(input())

    print(returnString)

