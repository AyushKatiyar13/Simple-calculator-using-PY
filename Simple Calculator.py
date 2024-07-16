from tkinter import E

while True:

    print("_____HELLO USER_____")

    print(   )

    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press e or E to exit")
    print("Press enter to continue") 

    print(   )

    choice = input("Choose your option : ")
    if choice == "e" or choice == "E":
        break

    num1=float(input("Enter your first number 1 : "))
    num2=float(input("Enter your second number 2 : "))

    if choice == "1":
        print(num1, "+", num2, "=", (num1 + num2))
    elif choice == "2":
        print(num1, "-", num2, "=", (num1 - num2))
    elif choice == "3":
        print(num1, "*", num2, "=", (num1 * num2))
    elif choice == "4":
        if num2 == 0:
            print(num1, "*", num2, "=", "not defined")
        else:
            print(num1, "/", num2, "=", (num1 / num2))

    else:
        print("invalid")
