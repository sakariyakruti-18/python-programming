a = float(input("Enter first number: "))

operator = input("Enter operator (+, -, *, /): ")

b = float(input("Enter second number: "))

match operator:

    case "+":
        print("Result:", a + b)

    case "-":
        print("Result:", a - b)

    case "*":
        print("Result:", a * b)

    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero is not allowed.")

    case _:
        print("Invalid operator.")

'''Enter first number: 8
Enter operator (+, -, *, /): /
Enter second number: 2
Result: 4.0'''