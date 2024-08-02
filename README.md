# Simple Calculator Program in Python 🧮

## Overview

This Python script implements a simple calculator capable of performing basic arithmetic operations such as addition, subtraction, multiplication, and division. Users interact with the program via a command-line interface, selecting an operation, inputting two numbers, and viewing the results. The script also provides an option to exit the program by pressing 'e' or 'E'.

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

1. **Importing Modules**:
   ```python
   from tkinter import E
   ```
   - This line imports the constant `E` from the `tkinter` module. However, in this script, `tkinter` is unnecessary and can be removed.

2. **Infinite Loop**:
   ```python
   while True:
   ```
   - This initiates an infinite loop to keep the calculator running until the user decides to exit.

3. **User Instructions**:
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
   - These lines display the menu options for the user to choose from.

4. **User Choice Input**:
   ```python
   choice = input("Choose your option : ")
   ```
   - Prompts the user to select an operation. If 'e' or 'E' is entered, the loop breaks, ending the program.

5. **Number Inputs**:
   ```python
   num1 = float(input("Enter your first number 1 : "))
   num2 = float(input("Enter your second number 2 : "))
   ```
   - Requests the user to input two numbers, which are converted to floating-point values for calculations.

6. **Performing Calculations**:
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
   - Based on the user's choice, the calculator performs the requested arithmetic operation:
     - **Addition**: Computes the sum of `num1` and `num2`.
     - **Subtraction**: Computes the difference between `num1` and `num2`.
     - **Multiplication**: Computes the product of `num1` and `num2`.
     - **Division**: Computes the quotient of `num1` divided by `num2`, with a check to avoid division by zero.

### GUI Consideration

The `tkinter` module is imported but not used in this script. Typically, `tkinter` is employed for creating graphical user interfaces. For a GUI version of this calculator, you could use `tkinter` to design buttons, input fields, and displays. Here’s a brief example of how you might start a `tkinter` GUI application:

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

## How to Run

1. **Save the Script**: Save the provided Python code in a file named `calculator.py`.
2. **Run the Script**: Open a terminal or command prompt, navigate to the directory containing `calculator.py`, and run:
   ```bash
   python calculator.py
   ```
3. **Interact with the Calculator**: Follow the on-screen instructions to perform calculations or exit the program.

## Thank you for exploring this simple calculator program! 😊🧮
