num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

def menu(num1, num2):
    while True:
        print("\n*** Main Menu ***")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 6.")
            continue

        if choice == 1:
            add = num1 + num2
            print(f"Addition of {num1} and {num2} is: {add}")
        
        elif choice == 2:
            sub = num1 - num2
            print(f"Subtraction of {num1} and {num2} is: {sub}")

        elif choice == 3:
            mul = num1 * num2
            print(f"Multiplication of {num1} and {num2} is: {mul}")

        elif choice == 4:
            if num2 != 0:
                div = num1 / num2
                print(f"Division of {num1} by {num2} is: {div}")
            else:
                print("Error: Cannot divide by zero!")

        elif choice == 5:
            if num2 != 0:
                mod = num1 % num2
                print(f"Modulus (Remainder) of {num1} by {num2} is: {mod}")
            else:
                print("Error: Cannot perform modulus with zero as the divisor!")

        elif choice == 6:
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

menu(num1, num2)
