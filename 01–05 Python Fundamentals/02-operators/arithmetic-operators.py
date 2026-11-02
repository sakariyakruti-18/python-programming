# Arithmetic Operators

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
else:
    print("Division, floor division, and modulus by zero are not allowed.")

print("Exponentiation:", a ** b)

'''
Enter first number: 12
Enter second number: 56
Addition: 68.0
Subtraction: -44.0
Multiplication: 672.0
Division: 0.21428571428571427
Floor Division: 0.0
Modulus: 12.0
Exponentiation: 2.717376270889602e+60
'''
