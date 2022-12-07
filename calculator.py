# Calculator
import math
def calcualtor():

        print("\t\t*************SIMPLE CALCULATOR************")
        print("\n\n")
        print(
            "1. Adding(+)\n"
            "2. Sbstraction(-)\n"
            "3. Multiplication(*)\n"
            "4. Division(/)\n"
            "5. Power values\n"
            "6. Square root\n"
            "7. COS value\n"
            "8. SIN value"
        )
        print("\n")
        a = int(input("Choose your choice : "))
        if a == 1:
            n1 = int(input("\nEnter the first number: "))
            n2 = int(input("Enter the second number: "))
            print("\nSum of two numbers : ", (n1 + n2))

        elif a == 2:
            n1 = int(input("\nEnter the first number: "))
            n2 = int(input("Enter the second number: "))
            print("\nDifference : ", (n1 - n2))

        elif a == 3:
            n1 = int(input("\nEnter the first number: "))
            n2 = int(input("Enter the second number: "))
            print("\nMultiplication : ", (n1 * n2))

        elif a == 4:
            n1 = int(input("\nEnter the first number: "))
            n2 = int(input("Enter the second number: "))
            print("\nDivision : ", (n1 / n2))

        elif a == 5:
            n1 = int(input("\nEnter the number: "))
            n2 = int(input("Enter the power value: "))
            print("\nAnswer : ",pow(n1,n2))

        elif a == 6:
            n1 = int(input("\nEnter the Square root value : "))
            print("\nSquare root value : ",(math.sqrt(n1)))

        elif a == 7:
            n1 = int(input("\nEnter the COS value : "))
            print("\nCOS","(",n1,") : ",(math.cos(n1)))

        elif a == 8:
            n1 = int(input("Enter the SIN value : "))
            print("\nSIN", "(", n1, ") : ", (math.sin(n1)))

        else:
            print("INVALID CHOICE!, PLEASE TRY AGAIN")

run = True
calcualtor()
while run:
    again = input("\nIf you want to calculate again[y/n] : ")
    if again in "Yy":
        calcualtor()
    else:
        run = False

