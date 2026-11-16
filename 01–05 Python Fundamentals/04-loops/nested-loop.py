rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print("*", end=" ")
    print()

'''Enter number of rows: 5
Enter number of columns: 10
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * *'''