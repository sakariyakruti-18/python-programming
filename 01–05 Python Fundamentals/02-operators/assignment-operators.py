# Assignment Operators using User Input

a = float(input("Enter a number: "))

print("Initial value:", a)

b = float(input("Enter a number to add: "))
a += b
print("After addition (+=):", a)

b = float(input("Enter a number to subtract: "))
a -= b
print("After subtraction (-=):", a)

b = float(input("Enter a number to multiply: "))
a *= b
print("After multiplication (*=):", a)

b = float(input("Enter a number to divide: "))

if b != 0:
    a /= b
    print("After division (/=):", a)
else:
    print("Cannot divide by zero.")

b = float(input("Enter a number for floor division: "))

if b != 0:
    a //= b
    print("After floor division (//=):", a)
else:
    print("Cannot perform floor division by zero.")

b = float(input("Enter a number for modulus: "))

if b != 0:
    a %= b
    print("After modulus (%=):", a)
else:
    print("Cannot perform modulus by zero.")

b = float(input("Enter an exponent: "))
a **= b
print("After exponentiation (**=):", a)

'''
Enter a number: 5
Initial value: 5.0
Enter a number to add: 6
After addition (+=): 11.0
Enter a number to subtract: 1
After subtraction (-=): 10.0
Enter a number to multiply: 5
After multiplication (*=): 50.0
Enter a number to divide: 12
After division (/=): 4.166666666666667
Enter a number for floor division: 4
After floor division (//=): 1.0
Enter a number for modulus: 0.2
After modulus (%=): 0.19999999999999996
Enter an exponent: 5
After exponentiation (**=): 0.00031999999999999965
'''
