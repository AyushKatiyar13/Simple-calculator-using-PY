Simple Calculator Program in Python

This Python script implements a simple calculator that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division. The user is prompted to select an operation and input two numbers, and the program will output the result. The user can continue performing calculations or exit the program by pressing 'e' or 'E'.

## Code Explanation

```python
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

    num1 = float(input("Enter your first number 1 : "))
    num2 = float(input("Enter your second number 2 : "))

    if choice == "1":
        print(num1, "+", num2, "=", (num1 + num2))
    elif choice == "2":
        print(num1, "-", num2, "=", (num1 - num2))
    elif choice == "3":
        print(num1, "", num2, "=", (num1  num2))
    elif choice == "4":
        if num2 == 0:
            print(num1, "/", num2, "=", "not defined")
        else:
            print(num1, "/", num2, "=", (num1 / num2))
    else:
        print("invalid")
```

### Detailed Breakdown

1. Importing Modules:
   ```python
   from tkinter import E
   ```
   This line imports the constant `E` from the `tkinter` module. Although `tkinter` is typically used for creating graphical user interfaces (GUIs), in this script, the `E` import is unnecessary and can be omitted.

2. Infinite Loop:
   ```python
   while True:
   ```
   This starts an infinite loop to keep the program running until the user decides to exit.

3. User Instructions:
   ```python
   print("_____HELLO USER_____")
   print(   )
   print("Press 1 for Addition")
   print("Press 2 for Subtraction")
   print("Press 3 for Multiplication")
   print("Press 4 for Division")
   print("Press e or E to exit")
   print("Press enter to continue")
   print(   )
   ```
   These lines print the menu options for the user to choose from.

4. User Choice Input:
   ```python
   choice = input("Choose your option : ")
   ```
   The program prompts the user to choose an option. If the user inputs 'e' or 'E', the loop breaks, ending the program.

5. Number Inputs:
   ```python
   num1 = float(input("Enter your first number 1 : "))
   num2 = float(input("Enter your second number 2 : "))
   ```
   The program asks the user to input two numbers, which are then converted to floating-point numbers for calculation.

6. Performing Calculations:
   ```python
   if choice == "1":
       print(num1, "+", num2, "=", (num1 + num2))
   elif choice == "2":
       print(num1, "-", num2, "=", (num1 - num2))
   elif choice == "3":
       print(num1, "", num2, "=", (num1  num2))
   elif choice == "4":
       if num2 == 0:
           print(num1, "/", num2, "=", "not defined")
       else:
           print(num1, "/", num2, "=", (num1 / num2))
   else:
       print("invalid")
   ```
   Based on the user's choice, the program performs the corresponding arithmetic operation:
   - Addition: Adds `num1` and `num2`.
   - Subtraction: Subtracts `num2` from `num1`.
   - Multiplication: Multiplies `num1` by `num2`.
   - Division: Divides `num1` by `num2` if `num2` is not zero. If `num2` is zero, it prints "not defined" to avoid division by zero.

### Why and How to Use This Module

Although the `tkinter` module is imported in this script, it is not utilized. Generally, `tkinter` is used for creating graphical user interfaces in Python. If you intend to create a GUI for this calculator, you would use `tkinter` to design buttons, input fields, and display areas for the calculator's interface. Here is an example of how you might start a `tkinter` GUI application:

```python
import tkinter as tk

def on_button_click(operation):
    # Define what happens when a button is clicked
    pass

root = tk.Tk()
root.title("Simple Calculator")

frame = tk.Frame(root)
frame.pack()

button_add = tk.Button(frame, text="Add", command=lambda: on_button_click("add"))
button_add.pack(side=tk.LEFT)

# Add more buttons for other operations

root.mainloop()
```

Thankyou 😊📊
