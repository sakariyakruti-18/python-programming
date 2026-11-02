# Logical Operators

age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("Eligible to vote:", age >= 18)
print("Passed:", marks >= 40)
print("Eligible for admission:", age >= 18 and marks >= 40)
print("Young or passed:", age < 18 or marks >= 40)
print("Not eligible to vote:", not (age >= 18))

'''
Enter your age: 21
Enter your marks: 89
Eligible to vote: True
Passed: True
Eligible for admission: True
Young or passed: True
Not eligible to vote: False
'''
