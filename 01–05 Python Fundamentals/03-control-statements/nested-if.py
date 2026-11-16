a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        print("Greatest number:", a)
    else:
        print("Greatest number:", c)
else:
    if b >= c:
        print("Greatest number:", b)
    else:
        print("Greatest number:", c)

'''Enter first number: 45
Enter second number: 9
Enter third number: 5896
Greatest number: 5896'''