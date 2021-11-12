
def func():
    print("Hello World")

def func1(name):
    print("Hi My name is {}".format(name))

def func3(x, y, z):
    if(z):
        return x
    else:
        return y

def func4(x, y):
    return x * y

def is_even(x):
    if(x % 2): #odd
        return False
    else:
        return True

def func6(x, y):
    if x > y:
        return True
    return False

def func7(*args):

    sum = 0

    for i in args:
        sum += i

    return sum

def func8(*args):

    ret_list = []

    for i in args:
        if is_even(i):
            ret_list.append(i)

    return ret_list


def func9(str):

    new_str = ''

    for  i in range(len(str)):
        if is_even(i): #value is even but the string character is odd, therefore treat is as odd.
            new_str += str[i].lower()
        else:
            new_str += str[i].upper()

    return new_str

def func10(num1, num2):
    if(is_even(num1) and is_even(num2) ):
        return min(num1, num2)
    else:
        return max(num1, num2)

def func11(x, y):
    if x.lower()[0] == y.lower()[0]:
        return True
    return False


def func13(str):

    ret_str = ''

    for index in range(len(str)):
        if index == 0 or index == 3:
            ret_str += str[index].upper()
            continue
        ret_str += str[index]

    return ret_str


if __name__ == '__main__' :

    func() #Problem 1

    print()

    func1("Ricky") #Problem 2
    
    print()
    
    print( func3('hello', 'goodbye', False) ) #Problem 3
    
    print()
    
    print( func4(3, 5) ) #Problem 4
    
    print()
   
    print(is_even(8)) #Problem 5

    print()

    print(func6(9, 10)) #Problem 6

    print()

    print(func7(1,2,3,4,5,6,7,8)) #Problem 7

    print()

    print(func8(1,2,3,4,5,6,7,8,9,10)) #Problem 8

    print()

    print(func9("Gary Oak")) #Problem 9

    print()

    print(func10(3, 5)) #Problem 10

    print()

    print(func11("Gary", "Ross")) #Problem 11

    print()

    print(func13("python")) #Problem 13

