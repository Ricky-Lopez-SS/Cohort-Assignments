
if __name__ == '__main__' :

    print("Part 1 \n")

    print(50+50)
    print(100-10)

    print("\nPart 2 \n")
 
    print(30+6)
    print(6^6)
    print(6 ** 6)
    print(6 + 6 + 6 + 6 + 6 + 6)

    print("\nPart 3\n")

    print("Hello World\n")
    print("Hello World : 10")

    print("\nPart 4 (Calculation)\n")

    P = float(input("Please input the initial loan amount.\n"))
    R = float(input("Please input the annual interest rate (in percent).\n")) * .01
    L = float(input("Please input the length of time you wish to pay off this loan in months.\n"))


    R = R / 12;

    M = P * (R * ( (1 + R) ** L) ) / (((1 + R) ** L) - 1)

    print("\n\n")
    print("The amount that should be paid every month is " , M)
