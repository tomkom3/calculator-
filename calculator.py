def calculator():
    print("Welcome to the Calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("Enter the operation number (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(f"The result is: {num1 + num2}")
            elif choice == '2':
                print(f"The result is: {num1 - num2}")
            elif choice == '3':
                print(f"The result is: {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"The result is: {num1 / num2}")
                else:
                    print("Division by zero is not allowed.")
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

calculator()
